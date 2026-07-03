import numpy as np


def runif(n, a, b):
    """Generate n uniform random variables on [a, b]."""
    return a + (b - a) * np.random.rand(n)
