import numpy as np


def frep2(X, x):
    """Empirical CDF of X evaluated at x."""
    return np.sum(np.asarray(X) <= x) / len(X)
