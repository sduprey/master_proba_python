import numpy as np


def discrete2(n, p):
    m = len(p)
    X = np.random.rand(n)
    p2 = np.cumsum(p)
    res = (X < p2[0]).astype(int)
    for i in range(1, m):
        res = res + (i + 1) * ((X > p2[i-1]) & (X < p2[i])).astype(int)
    return res
