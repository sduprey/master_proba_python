import numpy as np


def Ehrenfest(X, d):
    """Simulate one step of the Ehrenfest chain."""
    U = np.random.rand()
    return X + (U > X / d) - (U < X / d)
