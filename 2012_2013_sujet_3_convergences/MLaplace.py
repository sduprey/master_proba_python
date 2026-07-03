import numpy as np
from scipy.stats import binom


def MLaplace(n, p, x):
    """CDF of the standardised Binomial(n,p) evaluated at x."""
    return binom.cdf(np.array(x) * np.sqrt(n * p * (1 - p)) + n * p, n, p)
