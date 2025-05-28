# Uniform-Grid-On-Hypersphere

This repository contains a class (at `uniformonhypersphere.hypersphere.Hypersphere`) that allows to generate points on a unit hypersphere embedded in a $D$-dimensional space.

### Theoretical foundations

The mathematical derivations used to produce this code can be found [here](fibonacciSpiral.md)

### Installation

This package relies on the Python libraries listed in the [requirements file](requirements-full.txt) for its full functionalities. Though, if the aim is to use this code from within another projects, the strict requirements are [fewer](requirements.txt).

### Usage as a package

This package can be used directly from within another code. The only interface is the `Hypersphere` class, which provides the required coordinates in the form of a Numpy array. 

### Scripts

Two scripts are provided alongside with the core routines:
- `scripts/generate_random.py` to generate $N$ random points with uniform distribution on the hypersphere.
- `scripts/generate_fibonacci.py` to generate a close-to-uniform grid of points on the hypersphere using the Fibonacci spiral technique.
- `scripts/check_best_N.py` to plot the similarity between nearest neighbours in a Fibonacci spiral in $D$ dimensions over $N$ points. Since the Fibonacci spiral is not exaclty a uniform grid, and its deviation depends on $N$, several values of $N$ can be tested to check which one is "more uniform" in each specific use case.