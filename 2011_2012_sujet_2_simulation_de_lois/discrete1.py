import numpy as np


def discrete1(n):
    X = np.random.rand(n)
    return (X < 1/2).astype(int) + 2*((X > 1/2) & (X < 5/6)).astype(int) + 3*(X > 5/6).astype(int)
