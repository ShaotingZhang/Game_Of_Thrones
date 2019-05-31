# Game of Thrones

Graph modeling for the social network within episodes of Game of Thrones

## About this project

We build the social network graph in Game of Thrones and analyze the properties of the social network, such as centrality, diffusion. The Python vesion used here is 2.7. In this graph, each node represents a character in Game of Thrones. each edge of two nodes represents two character appear in the same screen in the script in the episodes. The weight of a edge represents how many times two person appear in the same screen.

## How to Run

```shell
git clone https://github.com/ShaotingZhang/Game_Of_Thrones
cd src
python2.7 1_step_generategraph.py # Collect the characters as nodes from specified url links. And build edges between nodes from scripts in the episodes
python2.7 2_step_Analysis.py # Analyze the attributes of the network.
python2.7 3_step_Diffusion.py # build the diffusion model and see how a message can be spread.
```

### Package dependencies (only tested on Mac OSX)

On Mac OS X, you may have an issue with running some packages, you may need to install them, especially for zen package.

```shell
pip install numpy
pip install scipy
pip install matplotlib
pip install networkx
pip install cython
pip install epydoc
```

Download the zen source as a zip file. https://github.com/networkdynamics/zenlib/archive/master.zip
Unzip this to a temporary location. Within Termianl navigate to the zenlib-master\src directory. Once sitting inside the zenlib-master\src directory, run the following command. This will compile and install zen.

```shell
python setup.py install
```
