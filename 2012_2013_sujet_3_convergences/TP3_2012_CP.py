"""TP3 2012-2013 Correction — Convergence, Moivre-Laplace."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom as binom_dist

from plotrep import plotrep
from runifd import runifd
from TCLde import TCLde
from MLaplace import MLaplace

# %% I. Convergence ps vers une constante
X = np.random.rand(1000)
M = np.zeros(1000)
M[0] = X[0]
for i in range(1, 1000):
    M[i] = max(M[i-1], X[i])
plt.figure(); plt.plot(M); plt.title('max(U_1,...,U_n) → 1'); plt.show()

# %% II. LGN
X = runifd(5000, 6)
S2 = np.cumsum(X) / np.arange(1, 5001)
plt.figure()
plt.plot(S2); plt.plot([0, 5000], [3.5, 3.5], 'r')
plt.title('LGN dé à 6 faces'); plt.show()

X2 = np.random.rand(5000)
S2b = np.cumsum(X2) / np.arange(1, 5001)
plt.figure()
plt.plot(S2b); plt.plot([0, 5000], [0.5, 0.5], 'r')
plt.show()

# %% III. Série aléatoire
plt.figure()
U = np.random.rand(30); E = (U < 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 31)); plt.plot(V)
U = np.random.rand(30); E = (U < 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 31)); plt.plot(V, 'r')
plt.show()

W = np.zeros(2000)
for i in range(2000):
    U = np.random.rand(30); E = (U < 0.5).astype(float)
    W[i] = np.sum(E / 2**np.arange(1, 31))
plt.figure(); plotrep(W); plt.title('Converge vers U[0,1]'); plt.show()

plt.figure()
U = np.random.rand(30); E = (U < 0.5).astype(float) + (-1)*(U > 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 31)); plt.plot(V)
U = np.random.rand(30); E = (U < 0.5).astype(float) + (-1)*(U > 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 31)); plt.plot(V, 'r')
plt.show()

W2 = np.zeros(2000)
for i in range(2000):
    U = np.random.rand(30); E = (U < 0.5).astype(float) + (-1)*(U > 0.5).astype(float)
    W2[i] = np.sum(E / 2**np.arange(1, 31))
plt.figure(); plotrep(W2); plt.show()

# %% IV. Moivre-Laplace
x = np.arange(-3, 3.1, 0.1)
plt.figure()
P = MLaplace(90, 0.8, x); P2 = norm.cdf(x)
plt.plot(x, P); plt.plot(x, P2, 'r'); plt.title('n=90, p=0.8'); plt.show()

plt.figure()
P = MLaplace(1000, 0.8, x)
plt.plot(x, P); plt.plot(x, P2, 'r'); plt.title('n=1000, p=0.8'); plt.show()

plt.figure()
P = MLaplace(90, 0.99, x)
plt.plot(x, P); plt.plot(x, P2, 'r'); plt.title('n=90, p=0.99'); plt.show()
