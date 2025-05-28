import os, sys
sys.path[0] = os.getcwd()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from uniformonhypersphere.hypersphere import Hypersphere
from uniformonhypersphere.helper import computeSimilarityMatrix, computeUniformity, sphericalToCartesian


def plotUniformityHeatmap():
	print("Plotting uniformity heatmap...")
	def kernel(dim, N):
		sphere = Hypersphere(dim)
		thetas = sphere.fibonacciSpiral(N)
		points = np.array([sphericalToCartesian(theta) for theta in thetas])
		return computeUniformity(points)
	Ns = 2**np.arange(4, 15)
	dims = np.arange(3, 10)
	values = np.zeros((len(dims), len(Ns)))
	for i, dim in enumerate(dims):
		for j, N in enumerate(Ns):
			print(f"{100/len(Ns)/len(dims)*(j+i*len(Ns)):.1f}%", flush=True, end="\r")
			values[i,j] = kernel(dim, N)
	print("Creating figure...", flush=True, end="\r")
	fig = plt.figure(figsize=(8,8))
	sb.heatmap(values, annot=True, fmt=".2f", xticklabels=Ns, yticklabels=dims)
	plt.xlabel("N")
	plt.ylabel("dim")
	plt.title("Uniformity of points on the hypersphere")
	fig.tight_layout()
	plt.savefig("tests/uniformity_heatmap.png")
	plt.show()


def plotSimilarityViolins():
	print("Plotting similarity violins...")
	def kernel(dim, N):
		sphere = Hypersphere(dim)
		thetas = sphere.fibonacciSpiral(N)
		points = np.array([sphericalToCartesian(theta) for theta in thetas])
		similarity_matrix = computeSimilarityMatrix(points)
		return np.nanmax(similarity_matrix, axis=1)
	dims = np.arange(3, 12, 2)
	Ns = 2**np.arange(4, 15)
	fig = plt.figure(figsize=(20,5))
	values = []
	for i, dim in enumerate(dims):
		for j, N in enumerate(Ns):
			newvalues = np.empty((N, 3))
			newvalues[:,0] = dim
			newvalues[:,1] = N
			newvalues[:,2] = kernel(dim, N)
			values.append(newvalues)
			print(f"{100/len(Ns)/len(dims)*(j+i*len(Ns)):.1f}%", flush=True, end="\r")
	values = np.concatenate(values, axis=0)
	df = pd.DataFrame(values, columns=["dim", "N", "similarity"])
	df["dim"] = df["dim"].astype("category")
	df["N"] = df["N"].astype(int)
	print("Creating figure...", flush=True, end="\r")
	sb.violinplot(data=df, x="N", y="similarity", hue="dim", cut=0, split=True, gap=0.2, density_norm="width", inner="quart")
	sb.set_style("whitegrid")
	plt.xlabel("N")
	plt.ylabel("NN similarity")
	plt.title("Distribution of similarity between NN of points on the grid")
	fig.tight_layout()
	plt.savefig("tests/similarity_violins.png")
	plt.show()


def plot3DSphere():
	print("Plotting 3D sphere...")
	sphere = Hypersphere(3)
	N = 100
	thetas = sphere.fibonacciSpiral(N)
	points = np.array([sphericalToCartesian(theta) for theta in thetas])
	fig = plt.figure(figsize=(8,8))
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(points[:,0], points[:,1], points[:,2])
	ax.set_xlabel("x")
	ax.set_ylabel("y")
	ax.set_zlabel("z")
	plt.title(f"{N} points on the 3D sphere")
	fig.tight_layout()
	plt.savefig("tests/3D_sphere.png")
	plt.show()


if __name__ == "__main__":
	plotUniformityHeatmap()
	plotSimilarityViolins()
	plot3DSphere()