import numpy as np


def Urne(Rouge, n, r, b):
    U = np.random.rand()
    return Rouge + (U < Rouge / (r + b + n))
