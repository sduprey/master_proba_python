import numpy as np
import matplotlib.pyplot as plt


def plotrep(X):
    """Draws the empirical CDF of X."""
    n = len(X)
    Y = np.sort(X)
    plt.step(Y, np.arange(1, n + 1) / n, where='post')
