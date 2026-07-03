"""Illustration de la convergence (Master MF 2010-2011)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom as binom_dist

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '2010_2011_sujet_3_convergences'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '2010_2011_sujet_2_simulation_de_lois'))

from plotrep import plotrep
from runifd import runifd
from TCLde import TCLde
from Markov import Markov

# %% Question 1
m = np.mean(np.arange(1, 7))
print(f'm={m}')

# %% Question 2-3
X = runifd(5000, 6)
S2 = np.cumsum(X) / np.arange(1, 5001)
plt.figure()
plt.plot(S2); plt.plot(m * np.ones(5000), 'r')
plt.title('LGN convergence')
plt.show()

# %% Question 4
plt.figure(); plt.plot(np.sqrt(np.arange(1, 5001)) * (S2 - m)); plt.show()
plt.figure(); plt.plot(np.arange(1, 5001) * (S2 - m)); plt.show()
plt.figure(); plt.plot((np.arange(1, 5001)**0.1) * (S2 - m)); plt.show()

# %% Question 5
plt.figure()
for n in [100, 500, 1000, 5000]:
    plotrep(X[:n])
plt.step(np.arange(1, 7), np.arange(1, 7)/6, 'r', where='post')
plt.show()

# %% Question 6
X2 = np.random.rand(5000)
S2b = np.cumsum(X2) / np.arange(1, 5001)
plt.figure(); plt.plot(S2b); plt.plot(0.5 * np.ones(5000)); plt.show()
plt.figure()
for n in [100, 500, 1000, 5000]:
    plotrep(X2[:n])
x01 = np.linspace(0, 1, 200)
plt.plot(x01, x01)
plt.show()

# %% Question 7-8-9-10
plt.figure()
U = np.random.rand(100); E = (U < 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 101)); plt.plot(V)
U = np.random.rand(100); E = (U < 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 101)); plt.plot(V, 'r')
plt.show()

# %% Question 11
sigma = np.sqrt(np.mean(np.arange(1, 7)**2) - m**2)
print(f'sigma={sigma}')
W = np.zeros(2000)
for i in range(2000):
    U = np.random.rand(30); E = (U < 0.5).astype(float)
    W[i] = np.sum(E / 2**np.arange(1, 31))
plt.figure(); plotrep(W); plt.show()

# %% Question 13
plt.figure()
U = np.random.rand(30); E = (U < 0.5).astype(float) + (-1)*(U > 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 31)); plt.plot(V)
U = np.random.rand(30); E = (U < 0.5).astype(float) + (-1)*(U > 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 31)); plt.plot(V, 'r')
plt.show()

W = np.zeros(2000)
for i in range(2000):
    U = np.random.rand(30); E = (U < 0.5).astype(float) + (-1)*(U > 0.5).astype(float)
    W[i] = np.sum(E / 2**np.arange(1, 31))
plt.figure(); plotrep(W); plt.show()

# %% TCL
for n in [10, 50, 300, 1000]:
    plt.figure(); TCLde(n, 1000); plt.title(f'TCL n={n}'); plt.show()

# %% Question 14 — Binomial → Poisson
a_arr = np.arange(9)
poi = np.exp(-2) * 2**a_arr / np.array([np.math.factorial(ai) for ai in a_arr])
plt.figure()
for n, p_val in [(10, 2/10), (100, 2/100), (1000, 2/1000)]:
    B = np.random.binomial(n, p_val, 5000)
    plotrep(B)
plt.step(a_arr, np.cumsum(poi), 'r', where='post')
plt.show()

# CDF comparison
plt.figure()
for n, p_val, col in [(10, 2/10, 'b'), (100, 2/100, 'r'), (1000, 2/1000, 'g')]:
    k = np.arange(11)
    plt.step(k, binom_dist.cdf(k, n, p_val), col, where='post')
plt.step(a_arr, np.cumsum(poi), 'k', where='post', label='Poisson')
plt.legend(); plt.show()

# %% Markov chain
A_mat = np.array([[0, 1/3, 2/3], [1/3, 0, 2/3], [2/3, 1/3, 0]])
P_vec = np.array([0.35, 0.25, 0.4])
print(P_vec @ A_mat)

p0 = np.array([0.05, 0.9, 0.05])
for n in [5, 10, 50, 100]:
    print(f'p{n} =', p0 @ np.linalg.matrix_power(A_mat, n))

Y = np.zeros(5000, dtype=int)
for n in range(5000):
    X = 1
    for k in range(1000):
        X = Markov(X)
    Y[n] = X
plt.figure()
plotrep(Y)
plt.step(np.arange(1, 4), np.cumsum(P_vec), 'r', where='post')
plt.show()
