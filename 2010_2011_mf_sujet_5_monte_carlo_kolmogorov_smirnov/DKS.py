import numpy as np
from scipy.stats import kstwobign


def DKS(X, F0, alpha):
    """One-sample Kolmogorov-Smirnov test. Returns p-value."""
    Y = F0(np.sort(X))
    n = len(X)
    Z1 = np.arange(1, n + 1) / n
    Z2 = np.arange(0, n) / n
    d1 = np.max(Z2 - Y)
    d2 = np.max(Y - Z1)
    d3 = max(d1, d2) * np.sqrt(n)
    ac = 1 - kstwobign.cdf(d3)
    rep = 'OUI' if ac > alpha else 'NON'
    print(rep)
    return ac
