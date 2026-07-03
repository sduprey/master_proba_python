"""Illustration de la convergence presque sure (2010-2011)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom as binom_dist

from plotrep import plotrep
from runifd import runifd
from TCLde import TCLde
from Markov import Markov

# %% Question 1
m = np.mean(np.arange(1, 7))
sigma = np.sqrt(np.mean(np.arange(1, 7)**2) - m**2)
print(f'm={m}, sigma={sigma}')

# %% Question 2
X = runifd(5000, 6)
S = np.cumsum(X)
S2 = S / np.arange(1, 5001)

# %% Question 3
plt.figure()
plt.plot(S2)
plt.plot(m * np.ones(5000))
plt.title('LGN — convergence de la moyenne empirique')
plt.show()

# %% Question 4
plt.figure()
plt.plot(np.sqrt(np.arange(1, 5001)) * (S2 - m))
plt.show()
plt.figure()
plt.plot(np.arange(1, 5001) * (S2 - m))
plt.show()
plt.figure()
plt.plot((np.arange(1, 5001)**0.1) * (S2 - m))
plt.show()

# %% Question 5
plt.figure()
plotrep(X[:100])
plotrep(X[:500])
plotrep(X[:1000])
plotrep(X[:5000])
plt.step(np.arange(1, 7), np.arange(1, 7)/6, 'r', where='post')
plt.title('CDF empirique — convergence ps')
plt.show()

# %% Question 6
X = np.random.rand(5000)
S = np.cumsum(X)
S2 = S / np.arange(1, 5001)
plt.figure()
plt.plot(S2)
plt.plot(0.5 * np.ones(5000))
plt.show()

plt.figure()
plotrep(X[:100])
plotrep(X[:500])
plotrep(X[:1000])
plotrep(X[:5000])
x01 = np.linspace(0, 1, 200)
plt.plot(x01, x01)
plt.show()

# %% Question 7-8-9-10
plt.figure()
U = np.random.rand(100)
E = (U < 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 101))
plt.plot(V)
U = np.random.rand(100)
E = (U < 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 101))
plt.plot(V, 'r')
plt.show()

# %% Question 11
W = np.zeros(2000)
for i in range(2000):
    U = np.random.rand(100)
    E = (U < 0.5).astype(float)
    W[i] = np.sum(E / 2**np.arange(1, 101))
plt.figure()
plotrep(W)
plt.show()

# %% Question 13
plt.figure()
U = np.random.rand(100)
E = (U < 0.5).astype(float) + (-1) * (U > 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 101))
plt.plot(V)
U = np.random.rand(100)
E = (U < 0.5).astype(float) + (-1) * (U > 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 101))
plt.plot(V, 'r')
plt.show()

W = np.zeros(2000)
for i in range(2000):
    U = np.random.rand(100)
    E = (U < 0.5).astype(float) + (-1) * (U > 0.5).astype(float)
    W[i] = np.sum(E / 2**np.arange(1, 101))
plt.figure()
plotrep(W)
plt.show()

# %% TCL
plt.figure()
TCLde(10, 1000); plt.title('TCL n=10'); plt.show()
plt.figure()
TCLde(50, 1000); plt.title('TCL n=50'); plt.show()
plt.figure()
TCLde(300, 1000); plt.title('TCL n=300'); plt.show()
plt.figure()
TCLde(1000, 1000); plt.title('TCL n=1000'); plt.show()

# %% Question 14 — Binomial → Poisson
a = np.arange(9)
poi = np.exp(-2) * 2**a / np.array([np.math.factorial(ai) for ai in a])
plt.figure()
for n, p_val in [(10, 2/10), (100, 2/100), (1000, 2/1000)]:
    B = np.random.binomial(n, p_val, 5000)
    plotrep(B)
plt.step(a, np.cumsum(poi), 'r', where='post')
plt.title('Convergence Binomiale → Poisson')
plt.show()

# %% Markov chain
A = np.array([[0, 1/3, 2/3], [1/3, 0, 2/3], [2/3, 1/3, 0]])
P = np.array([0.35, 0.25, 0.4])
print(P @ A)

p0 = np.array([0.05, 0.9, 0.05])
print('p5  =', p0 @ np.linalg.matrix_power(A, 5))
print('p10 =', p0 @ np.linalg.matrix_power(A, 10))
print('p50 =', p0 @ np.linalg.matrix_power(A, 50))
print('p100=', p0 @ np.linalg.matrix_power(A, 100))

p0 = np.array([0, 1, 0])
print(p0 @ np.linalg.matrix_power(A, 10))
print(p0 @ np.linalg.matrix_power(A, 50))

Y = np.zeros(5000, dtype=int)
for n in range(5000):
    X = 1
    for k in range(1000):
        X = Markov(X)
    Y[n] = X

plt.figure()
plotrep(Y)
plt.step(np.arange(1, 4), np.cumsum(P), 'r', where='post')
plt.title('Loi stationnaire chaîne de Markov')
plt.show()
