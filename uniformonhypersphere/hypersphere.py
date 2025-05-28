import numpy as np
from scipy.optimize import root_scalar
from scipy.special import gamma
from uniformonhypersphere.helper import computePrimes


class Hypersphere:
	"""
	Class to generate points uniformly on a hypersphere.
	"""
	def __init__(self, dim: int):
		"""
		Initialize the hypersphere with the given dimension.

		Parameters
		----------
		dim : int
			The dimension of the hypersphere.
		"""
		self.dim = dim


	def randomSample(self, N: int, rng = None) -> np.ndarray:
		"""
		Generate random points uniformly distributed on the hypersphere.

		Parameters
		----------
		N : int
			The number of points to generate.
		
		rng : np.random.Generator, optional
			Random number generator for reproducibility. If None, a new generator is created.

		Returns
		-------
		points : np.ndarray
			The angular coordinates of the random points on the hypersphere.
		"""
		if rng is None:
			rng = np.random.default_rng()
		cumulatives = rng.uniform(0, 1, (N, self.dim-1))
		return self.__computeThetas(N, cumulatives)


	def fibonacciSpiral(self, N: int) -> np.ndarray:
		"""
		Generate a grid on the hypersphere using the Fibonacci spiral method.

		Parameters
		----------
		N : int
			The number of points to generate.

		Returns
		-------
		points : np.ndarray
			The angular coordinates of the grid points on the hypersphere.
		"""
		cumulatives = self.__computeCumulativesSpiral(N)
		return self.__computeThetas(N, cumulatives)
	

	def __computeThetas(self, N, cumulatives):
		thetas = np.zeros((N, self.dim-1))
		for i in range(self.dim-1):
			for k in range(N):
				thetas[k,i] = root_scalar(self.__implicit, args=(cumulatives[k,i],self.dim-2-i), bracket=self.__getBracket(i)).root
		return thetas
	

	def __getBracket(self, i):
		if i == self.dim-2:
			return [0, 2 * np.pi]
		else:
			return [0, np.pi]


	def __computeCumulativesSpiral(self, N):
		cumulatives = np.zeros((N, self.dim-1))
		ks = np.arange(1, N+0.5)
		cumulatives[:,-1] = (ks - 0.5) / N
		cs = np.sqrt(computePrimes(self.dim-2))
		for i in range(self.dim-2):
			cumulatives[:,i] = (ks * cs[i]) % 1
		return cumulatives
	

	def __integral(self, theta, n):
		if n == 0:
			return theta
		if n == 1:
			return 1 - np.cos(theta)
		return (-1/n) * np.sin(theta)**(n-1) * np.cos(theta) + (n-1)/n * self.__integral(theta, n-2)


	def __implicit(self, theta, Y, n):
		if n == 0:
			return Y - self.__integral(theta, n) / (2 * np.pi)
		return Y - self.__integral(theta, n) * 1/np.sqrt(np.pi) * (gamma((n+2)/2))/(gamma((n+1)/2))
