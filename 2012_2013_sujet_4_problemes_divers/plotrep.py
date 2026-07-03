import numpy as np
import matplotlib.pyplot as plt


def plotrep(X):
    n = len(X)
    Y = np.sort(np.asarray(X, dtype=float))
    plt.step(Y, np.arange(1, n + 1) / n, where='post')
