import zen
import scipy.integrate as spi
import matplotlib.pyplot as plt
plt.ioff()
import numpy
from math import e
from numpy import *
from numpy.linalg import eig,norm
import sys
sys.path.insert(0, '../zend3js/')
import d3js
from time import sleep
import colorsys
import numpy.linalg as la


def print_top(G, v, num=10):
    idx_list = [(i,v[i]) for i in range(len(v))]
    idx_list = sorted(idx_list, key = lambda x: x[1], reverse=True)
    for i in range(min(num,len(idx_list))):
        nidx, score = idx_list[i]
        print ("%i. %s (%1.4f)" % (i+1,G.node_object(nidx),score))

def index_of_max(v):
    return numpy.where(v == max(v))[0]

def calc_powerlaw(G, kmin):
    N = G.num_nodes
    ddist = zen.degree.ddist(G,normalize=False)
    cdist = zen.degree.cddist(G,inverse=True)
    k = numpy.arange(len(ddist))

    plt.figure(figsize=(10,8))
    plt.subplot(211)
    plt.bar(k,ddist, width=0.8, bottom=0, color='b')
    plt.xlabel("Degree")
    plt.ylabel("Degree Distribution")

    plt.subplot(212)
    plt.loglog(k,cdist)
    plt.xlabel("Degree")
    plt.ylabel("Cumulative Degree Distribution")

    sub = 0
    for z in range(0,len(ddist) - 1):
        if z < kmin:
            sub = sub + ddist[z]
    N = G.num_nodes - sub

    sum = 0
#     print ddist
#     print len(ddist)
    for k_i in range(kmin, len(ddist) - 1):
        fraction = k_i / (kmin - 0.5)
        iLn = ddist[k_i] * math.log(fraction,e)
        sum = sum + iLn
        if (sum != 0):
            sum_inv = 1/sum
    alpha = 1 + N * sum_inv # calculate using formula!
    print ('alpha is %1.2f' %alpha) 
    plt.show()



def main():
    G = zen.io.gml.read('GameOfThrones.gml',weight = True, directed = False)



    A = G.matrix()
    N = G.num_nodes

    print ('\n=============================================')
    print ('\nDegree Centrality:')
    vv = [0] * N
    for i in range(N):
            v1 = G.neighbors_(i)
            sum = 0
            for j in range(len(v1)):
                    sum += G.weight(G.node_object(i),G.node_object(v1[j]))
            vv[i] = sum
    print_top(G,vv)

    print ('\n=============================================')
    # Eigenvector Centrality
    print ('\nEigenvector Centrality (by Zen):')
    v2 = zen.algorithms.centrality.eigenvector_centrality_(G,weighted = True)
    print_top(G,v2)

    print ('\n=============================================')
    # Betweenness Centrality
    print ('\nBetweenness Centrality')
    v = zen.algorithms.centrality.betweenness_centrality_(G)
    print_top(G,v)


    print ('\n==============================================')
    print ('\nPOWER LAW')
    calc_powerlaw(G,3)    # need to change kmin appropriately


    print ('\n==============================================')
    print ('\nClustering Coefficients')
    c = zen.algorithms.clustering.gcc(G)
    print ('Clustering: %s' % c)



if __name__ == '__main__':
    main()
