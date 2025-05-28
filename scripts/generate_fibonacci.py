import os, sys
sys.path[0] = os.getcwd()


import numpy as np
from argparse import ArgumentParser
from uniformonhypersphere.hypersphere import Hypersphere
from uniformonhypersphere.helper import sphericalToCartesian


if __name__ == "__main__":
	parser = ArgumentParser(description="Generate grid of points on a hypersphere using Fibonacci Spiral.")
	parser.add_argument("-d", "--dim", type=int, required=True, help="Dimensionality of the embedding space.")
	parser.add_argument("-n", "--npoints", type=int, required=True, help="Number of points in the grid.")
	parser.add_argument("-o", "--output", type=str, default=None, help="Output file for the points. If not specified, the points will be printed to stdout.")
	parser.add_argument("-c", "--carthesian", action="store_true", help="Output points in Cartesian coordinates instead of spherical coordinates.")
	args = parser.parse_args()

	dim = args.dim
	if dim < 2:
		raise ValueError("Dimension must be at least 2.")
	
	N = args.npoints
	if N < 1:
		raise ValueError("Number of points must be at least 1.")
	
	sphere = Hypersphere(dim)
	points = sphere.fibonacciSpiral(N)
	header = ",".join([f"theta_{i+1}" for i in range(points.shape[1])])

	if args.carthesian:
		points = np.array([sphericalToCartesian(x) for x in points])
		header = ",".join([f"x_{i+1}" for i in range(points.shape[1])])

	if args.output is None:
		print(header)
		for p in points:
			print(",".join([f"{x:.16f}" for x in p]))
	else:
		np.savetxt(args.output, points, delimiter=",", header=header, comments="")