import numpy as np


def Ehrenfest2(X, d):
    """Simulate one step of the lazy Ehrenfest chain."""
    U = np.random.rand()
    if U < d / (d + 1):
        V = np.random.rand()
        X = X + (V > X / d) - (V < X / d)
    return X
