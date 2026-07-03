import numpy as np


def rbernou(n, m, p):
    """Generate an n x m matrix of Bernoulli(p) random variables."""
    return (np.random.rand(n, m) < p).astype(int)
