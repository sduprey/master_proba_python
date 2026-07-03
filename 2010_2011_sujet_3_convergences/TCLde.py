import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from plotrep import plotrep


def TCLde(n, Nobs):
    V = np.zeros(Nobs)
    for i in range(Nobs):
        X = np.random.randint(1, 7, n)
        V[i] = (np.sum(X) / n - 3.5) * np.sqrt(n) / np.sqrt(17.5 / 6)
    plotrep(V)
    x = np.linspace(-3, 3, 200)
    plt.plot(x, norm.cdf(x), 'r')
