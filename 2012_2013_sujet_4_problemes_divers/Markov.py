import numpy as np


def Markov(X):
    U = np.random.rand()
    if X == 1:
        Y = 2 * (U < 1/3) + 3 * (U > 1/3)
    elif X == 2:
        Y = 1 * (U < 1/3) + 3 * (U > 1/3)
    elif X == 3:
        Y = 1 * (U < 2/3) + 2 * (U > 2/3)
    else:
        Y = X
    return int(Y)
