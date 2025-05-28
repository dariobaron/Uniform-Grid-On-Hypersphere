import os, sys
sys.path[0] = os.getcwd()

from uniformonhypersphere.hypersphere import Hypersphere


def test_integrals():
	import numpy as np

	thetas = np.array([0.5, 0.8, 1.3]) * np.pi
	ns = np.array([3, 5, 10, 100])

	integrals = [
		0.666667, 1.29918, 1.18676,
		0.533333, 1.05866, 0.999768,
		0.386563, 0.772813, 0.786515,
		0.125018, 0.250037, 0.250037
	]

	sphere = Hypersphere(3)
	results = np.array([[sphere._Hypersphere__integral(theta, n) for theta in thetas] for n in ns])

	assert np.allclose(integrals, results.flatten(), atol=1e-4), f"Expected {integrals}, got {results.flatten()}"


def test_normalization():
	import numpy as np

	ns = np.arange(1,50)

	sphere = Hypersphere(3)
	results = np.array([sphere._Hypersphere__implicit(np.pi,1,n) for n in ns])

	assert np.allclose(results, 0, atol=1e-8), f"Expected 0, got {results}"