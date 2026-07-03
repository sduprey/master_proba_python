import numpy as np
from scipy.stats import norm


def Intconf(X, s, alpha):
    """Confidence interval for the mean with known std s."""
    t = norm.ppf(1 - alpha / 2)
    n = len(X)
    m = np.mean(X)
    return np.array([m - s * t / np.sqrt(n), m + s * t / np.sqrt(n)])
