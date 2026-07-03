import numpy as np
import matplotlib.pyplot as plt

from Fattente import Fattente
from plim import plim
from plotrep import plotrep


def convattente(p, q):
    plt.clf()
    Y = np.zeros((5, 2000))
    X = np.zeros(500, dtype=int)
    for k in range(2000):
        X[0] = 0
        for n in range(1, 500):
            X[n] = Fattente(X[n - 1], p, q)
        Y[0, k] = X[9]
        Y[1, k] = X[19]
        Y[2, k] = X[49]
        Y[3, k] = X[149]
        Y[4, k] = X[499]
    for k in range(5):
        plotrep(Y[k, :])
    if p < q:
        pconv = plim(p, q)
        plt.step(np.arange(15), np.cumsum(pconv), 'r', where='post')
