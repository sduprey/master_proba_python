import numpy as np
import matplotlib.pyplot as plt

from Fattente import Fattente
from plim import plim


def plotergo(p, q, nmax):
    plt.clf()
    X = np.zeros(nmax, dtype=int)
    for k in range(1, nmax):
        X[k] = Fattente(X[k - 1], p, q)
    plimite = plim(p, q)
    fig, axes = plt.subplots(3, 5, figsize=(15, 9))
    for m in range(15):
        ax = axes[m // 5, m % 5]
        erg = np.cumsum(X == m) / np.arange(1, nmax + 1)
        ax.plot(erg)
        ax.axhline(plimite[m], color='r')
        ax.set_title(f'm={m}')
    plt.tight_layout()
