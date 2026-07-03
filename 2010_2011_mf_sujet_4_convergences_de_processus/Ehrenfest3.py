import numpy as np


def Ehrenfest3(d, X):
    """Simulate one step of the lazy Ehrenfest chain (aperiodic version)."""
    U = np.random.rand()
    if U < d / (d + 1):
        V = np.random.rand()
        Y = X + (V > X / d) - (V < X / d)
    else:
        Y = X
    return Y
