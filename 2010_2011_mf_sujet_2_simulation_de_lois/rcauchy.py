import numpy as np


def rcauchy(n):
    """Generate n samples from a Cauchy distribution via CDF inversion."""
    X = np.random.rand(n)
    return -np.tan(np.pi * (X - 0.5))
