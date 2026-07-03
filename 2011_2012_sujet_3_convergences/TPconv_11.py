"""Illustration de la convergence — 2011-2012."""
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
plt.plot(S2); plt.plot(m * np.ones(5000))
plt.title('LGN'); plt.show()

# %% Question 4
plt.figure(); plt.plot((np.arange(1, 5001)**0.1) * (S2 - m)); plt.show()
plt.figure(); plt.plot(np.arange(1, 5001) * (S2 - m)); plt.show()
plt.figure(); plt.plot(np.sqrt(np.arange(1, 5001)) * (S2 - m)); plt.show()

# %% Question 5
plt.figure()
for n in [100, 500, 1000, 5000]:
    plotrep(X[:n])
plt.step(np.arange(1, 7), np.arange(1, 7)/6, 'r', where='post')
plt.show()

# %% Question 6-7-8-9
plt.figure()
U = np.random.rand(100); E = (U < 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 101)); plt.plot(V)
U = np.random.rand(100); E = (U < 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 101)); plt.plot(V, 'r')
plt.show()

# %% Question 10
W = np.zeros(2000)
for i in range(2000):
    U = np.random.rand(100); E = (U < 0.5).astype(float)
    W[i] = np.sum(E / 2**np.arange(1, 101))
plt.figure(); plotrep(W); plt.show()

# %% Question 12
plt.figure()
U = np.random.rand(100); E = (U < 0.5).astype(float) + (-1)*(U > 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 101)); plt.plot(V)
U = np.random.rand(100); E = (U < 0.5).astype(float) + (-1)*(U > 0.5).astype(float)
V = np.cumsum(E / 2**np.arange(1, 101)); plt.plot(V, 'r')
plt.show()

W = np.zeros(2000)
for i in range(2000):
    U = np.random.rand(100); E = (U < 0.5).astype(float) + (-1)*(U > 0.5).astype(float)
    W[i] = np.sum(E / 2**np.arange(1, 101))
plt.figure(); plotrep(W); plt.show()

# %% Question 13 — Moivre-Laplace approximation
k = np.arange(200, 401)
plt.figure()
plt.stem(k, binom_dist.pmf(k, 1000, 0.3), basefmt=' ', markerfmt='b.', linefmt='b-')
x = np.linspace(200, 400, 200)
plt.plot(x, norm.pdf(x, 1000*0.3, np.sqrt(1000*0.3*0.7)), 'r')
plt.show()

# %% Question 14 — TCL
for n_val in [10, 50, 300, 1000]:
    plt.figure(); TCLde(n_val, 1000); plt.title(f'TCL n={n_val}'); plt.show()

# %% Question 15 — Binomial → Poisson
a_arr = np.arange(9)
poi = np.exp(-2) * 2**a_arr / np.array([np.math.factorial(ai) for ai in a_arr])
plt.figure()
for n_val, p_val in [(10, 2/10), (100, 2/100), (1000, 2/1000)]:
    B = np.random.binomial(n_val, p_val, 5000)
    plotrep(B)
plt.step(a_arr, np.cumsum(poi), 'r', where='post')
plt.show()
