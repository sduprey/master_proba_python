import numpy as np


def me(v):
    return np.mean(v), np.std(v, ddof=1)
