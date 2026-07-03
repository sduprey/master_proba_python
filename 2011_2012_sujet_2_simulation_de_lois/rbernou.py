import numpy as np


def rbernou(n, m, p):
    return (np.random.rand(n, m) < p).astype(int)
