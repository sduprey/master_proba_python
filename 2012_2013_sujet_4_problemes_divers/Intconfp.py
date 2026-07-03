import numpy as np
from scipy.stats import norm


def Intconfp(N, n, a):
    """Confidence interval for a proportion (poll/survey)."""
    m = n / N
    s = np.sqrt(m * (1 - m))
    t = norm.ppf(1 - a / 2)
    return np.array([m - s * t / np.sqrt(N), m + s * t / np.sqrt(N)])
