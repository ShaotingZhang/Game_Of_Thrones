# Game of Thrones

Small project of Game of Thrones in Python 2.7 in OSX

## About this project

We build the social network graph in Game of Thrones. The vesion of python is 2.7. If you use python 3.*, it may have some problems. 

## How to Run

```shell
git clone https://github.com/ShaotingZhang/Game_Of_Thrones
cd src
python2.7 1_step_generategraph.py
python2.7 2_step_Analysis.py
python2.7 3_step_Diffusion.py
```

### Mac

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
sudo python setup.py install
```
The zen source need to be installed after others packages have been installed.

