import numpy as np


def sphericalToCartesian(thetas):
	dim = thetas.shape[0] + 1
	x = np.full(dim, 1.)
	for i in range(dim):
		if i != 0:
			x[i] = x[i] * np.cos(thetas[dim-1-i])
		for j in range(dim-1-i):
			x[i] = x[i] * np.sin(thetas[j])
	return x


def computePrimes(n):
	primes = set()
	primes.add(2)
	candidate = 3
	while len(primes) < n:
		is_prime = True
		for p in primes:
			if candidate % p == 0:
				is_prime = False
				break
		if is_prime:
			primes.add(candidate)
		candidate += 2
	return np.sort(np.array(list(primes)))


def computeSimilarityMatrix(arr):
	n = arr.shape[0]
	matrix = np.zeros((n, n))
	for i in range(n):
		for j in range(i+1,n):
			matrix[i,j] = np.dot(arr[i], arr[j])
	matrix = matrix + matrix.T
	matrix[np.diag_indices(n)] = np.nan
	return matrix


def computeUniformity(arr):
	similarity_matrix = computeSimilarityMatrix(arr)
	nearest_neighbours = np.nanmin(similarity_matrix, axis=1)
	return nearest_neighbours.max() - nearest_neighbours.min()