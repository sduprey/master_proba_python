"""KS deux échantillons et régression linéaire — Master MF 2010-2011."""
import numpy as np
import matplotlib.pyplot as plt

from frep2 import frep2
from DKS2 import DKS2
from regr import regr
from regr2 import regr2
from plotrep import plotrep

def _plotrep(X):
    n = len(X)
    Y = np.sort(np.asarray(X, dtype=float))
    plt.step(Y, np.arange(1, n+1)/n, where='post')

# %% KS deux échantillons
X = np.random.rand(100)
print('frep2(X, 0.4) =', frep2(X, 0.4))

Y = np.random.rand(200)
print('KS U[0,1] vs U[0,1]:', DKS2(X, Y, 0.05))

Y = np.random.randn(90)
print('KS U[0,1] vs N(0,1):', DKS2(X, Y, 0.05))

# Real dataset (Table 1)
X_data = np.array([0.2, 3.8, 7.6, 4, 4.1, -2.8, 4.7, 3.6, 5.4, -0.2,
                   1.6, 5.6, -0.6, 0.8, -5, 0.1, 2.9, 3.7, 3.9, 1.1])
Y_data = np.array([1.8, 4, 1.4, 1.9, 1.8, 1.4, 1.9, 1.4, 4.5, 2.2,
                   2.4, 3.1, 0.3, -1.4, 0.4, 2.3, 0.2, 1.5, 4.8, 0.6,
                   1, 1.5, 5.5])
plt.figure()
_plotrep(X_data); _plotrep(Y_data)
plt.title('CDF empiriques X et Y')
plt.show()
print('KS X_data vs Y_data:', DKS2(X_data, Y_data, 0.05))

# %% Régression linéaire
X_lin = np.arange(1, 51) / 50
Y_lin = 1 + 2 * X_lin + 0.5 * np.random.randn(50)
regr(Y_lin, X_lin)
plt.show()

# %% Régression multiple — note: getdata() is a stixbox function not available here.
# To use with real data, load a numpy array: MX = np.loadtxt('data_file.txt')
# regr2(Y, MX)
print('Note: regr2 example requires external data (getdata not available in Python).')
print('Usage: regr2(Y_array, X_matrix)')
