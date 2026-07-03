import numpy as np


def runif(n, a, b):
    return a + (b - a) * np.random.rand(n)
