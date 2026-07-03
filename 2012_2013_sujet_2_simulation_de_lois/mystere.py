import numpy as np


def mystere(p):
    """Generate a geometric(p) random variable (number of trials until first success)."""
    k = 1
    while np.random.rand() > p:
        k += 1
    return k
