import numpy as np


def plim(p, q):
    """Stationary distribution of the M/Geo/1 queue (truncated to 15 states)."""
    res = np.zeros(15)
    res[0] = 1 - p / q
    idx = np.arange(1, 15)
    res[1:] = (1 / (1 - q)) * (1 - p / q) * (p / q)**idx * ((1 - q) / (1 - p))**idx
    return res
