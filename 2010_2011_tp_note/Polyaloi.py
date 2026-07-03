import numpy as np

from Urne import Urne


def Polyaloi(nech, n, r, b):
    X = np.zeros(nech)
    for k in range(nech):
        X[k] = r / (r + b)
        for l in range(1, n + 1):
            X[k] = Urne(X[k] * (r + b + l - 1), l - 1, r, b) / (r + b + l)
    return X
