import numpy as np

from Urne import Urne


def Polya(n, r, b):
    R = np.zeros(n + 1)
    R[0] = r
    for k in range(1, n + 1):
        R[k] = Urne(R[k - 1], k - 1, r, b)
    return R
