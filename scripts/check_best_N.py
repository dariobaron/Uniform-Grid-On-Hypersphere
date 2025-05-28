import os, sys
sys.path[0] = os.getcwd()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from argparse import ArgumentParser
from uniformonhypersphere.hypersphere import Hypersphere
from uniformonhypersphere.helper import computeSimilarityMatrix, sphericalToCartesian


def splitInput(input):
	"""
	Split the input string into a list of integers.
	"""
	ns = []
	try:
		ns.append(int(input))
	except:
		input = input.split(",")
		for i in input:
			try:
				ns.append(int(i))
			except:
				range_ = i.split(":")
				try:
					if len(range_) == 2:
						start,stop = range_
						ns.extend(range(int(start),int(stop)))
					elif len(range_) == 3:
						start,stop,step = range_
						ns.extend(range(int(start),int(stop),int(step)))
					else:
						raise ValueError(f"Invalid range: {i}. Must be of the form start:stop or start:stop:step.")
				except:
					raise ValueError(f"Invalid input: {input}. Must be a single or a comma-separated list, of integers or of ranges in the form start:stop[:step].")
	return ns


def kernel(N, sphere):
		thetas = sphere.fibonacciSpiral(N)
		points = np.array([sphericalToCartesian(theta) for theta in thetas])
		similarity_matrix = computeSimilarityMatrix(points)
		return np.nanmax(similarity_matrix, axis=1)


if __name__ == "__main__":
	parser = ArgumentParser(description="Generate a NN similarity plot for different values of n.")
	parser.add_argument("-d", "--dim", type=int, required=True, help="Dimensionality of the embedding space.")
	parser.add_argument("-n", "--npoints", type=str, required=True, help="Number of points to evaluate. Must be a single or a comma-separated list, of integers or of ranges in the form start:stop[:step].")
	parser.add_argument("-o", "--output", type=str, default=None, help="Output file for the figure. If not specified, the figure will be shown in a window.")
	args = parser.parse_args()

	dim = args.dim
	if dim < 2:
		raise ValueError("Dimension must be at least 2.")
	
	Ns = splitInput(args.npoints)
	
	sphere = Hypersphere(dim)

	fig = plt.figure(figsize=(max(2+0.3*len(Ns),6),5))

	values = []
	for i, N in enumerate(Ns):
		newvalues = np.empty((N, 2))
		newvalues[:,0] = N
		newvalues[:,1] = kernel(N, sphere)
		values.append(newvalues)
		print(f"Computing values: {100/len(Ns)*i:.1f}%", flush=True, end="\r")
	values = np.concatenate(values, axis=0)
	df = pd.DataFrame(values, columns=["N", "similarity"])
	df["N"] = df["N"].astype(int)

	print("Creating figure...", flush=True, end="\r")
	sb.violinplot(data=df, x="N", y="similarity", cut=0, split=False, gap=0.2, density_norm="width", inner="quart")
	sb.set_style("whitegrid")
	plt.xlabel("N")
	plt.ylabel("NN similarity")
	plt.title("Distribution of similarity\nbetween NN of points on the grid")
	fig.tight_layout()

	if args.output is None:
		plt.show()
	else:
		plt.savefig(args.output)
		print(f"Figure saved to {args.output}")
