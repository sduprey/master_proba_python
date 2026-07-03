import numpy as np


def rbernou(n, p):
    """Generate n samples from a Bernoulli(p) distribution."""
    return (np.random.rand(n) < p).astype(int)
