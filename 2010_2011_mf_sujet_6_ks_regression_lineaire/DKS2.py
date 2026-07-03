import numpy as np
from scipy.stats import kstwobign

from frep2 import frep2


def DKS2(X, Y, alpha):
    """Two-sample Kolmogorov-Smirnov test. Returns p-value and decision."""
    n, m = len(X), len(Y)
    Z = np.sort(np.concatenate([X, Y]))
    T = np.array([abs(frep2(X, z) - frep2(Y, z)) for z in Z])
    d = np.sqrt(n * m / (n + m)) * np.max(T)
    print(f'd = {d}')
    ac = 1 - kstwobign.cdf(d)
    rep = 'OUI' if ac > alpha else 'NON'
    print(rep)
    return ac, rep
