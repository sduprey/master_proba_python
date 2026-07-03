import numpy as np


def runifd(n, N):
    """Generate n samples of discrete uniform distribution on {1, ..., N}."""
    return np.random.randint(1, N + 1, n)
