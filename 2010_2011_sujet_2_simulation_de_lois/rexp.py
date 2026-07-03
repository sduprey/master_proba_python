import numpy as np


def rexp(n, l):
    """Generate n samples of exponential distribution with rate l."""
    return -np.log(np.random.rand(n)) / l
