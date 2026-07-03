import numpy as np
from scipy.stats import norm


def sondage(N, n):
    """Proportion estimate and p-value for testing p=0.5."""
    p = n / N
    s = np.sqrt(p * (1 - p))
    re = np.zeros(2)
    re[0] = p
    re[1] = 2 * (1 - norm.cdf(abs(0.5 - p) * np.sqrt(N) / s))
    return re
