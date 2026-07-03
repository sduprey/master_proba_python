import numpy as np


def Fattente(X, p, q):
    Y = int(np.random.rand() < p)
    if X == 0:
        return Y
    else:
        Z = int(np.random.rand() < q)
        return X + Y - Z
