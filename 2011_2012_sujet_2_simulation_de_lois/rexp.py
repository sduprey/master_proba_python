import numpy as np


def rexp(n, l):
    return -np.log(np.random.rand(n)) / l
