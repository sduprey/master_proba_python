"""TP noté 2010-2011 — Polya, Ehrenfest, Markov."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom as binom_dist

from plotrep import plotrep
from Urne import Urne
from Polya import Polya
from Polyaloi import Polyaloi
from Ehrenfest import Ehrenfest
from Ehrenfest2 import Ehrenfest2

def _plotrep_local(X):
    n = len(X)
    Y = np.sort(np.asarray(X, dtype=float))
    plt.step(Y, np.arange(1, n+1)/n, where='post')

# %% Exercice 1 — Rejection (unit disk)
X = np.random.rand(10000)
Y = np.random.rand(10000)
I = np.where(X**2 + Y**2 < 1)[0]
Xd, Yd = X[I], Y[I]
plt.figure()
plt.plot(Xd, Yd, 'd', ms=1)
t = np.linspace(0, np.pi/2, 200)
plt.plot(np.cos(t), np.sin(t))
plt.axis('equal')
plt.show()

# %% 2
plt.figure()
_plotrep_local(np.sqrt(Xd**2 + Yd**2))
x = np.linspace(0, 1, 200)
plt.plot(x, x**2, 'r')
plt.show()

# %% 3
plt.figure()
_plotrep_local(Xd)
x = np.linspace(0, 1, 200)
plt.plot(x, 2/np.pi * (np.arcsin(x) + x * np.sqrt(1 - x**2)), 'r')
plt.show()

# %% Exercice 2 — Cauchy
n = 1000
X = np.random.rand(n)
Y = np.tan(np.pi * (X - 0.5))
M = np.cumsum(Y) / np.arange(1, n+1)
plt.figure(); plt.plot(M); plt.title('Moyenne de Cauchy — pas de convergence'); plt.show()

n, Nech = 500, 2000
M = np.zeros(Nech)
for k in range(Nech):
    X = np.random.rand(n)
    M[k] = np.mean(np.tan(np.pi * (X - 0.5)))
plt.figure()
_plotrep_local(M)
x = np.linspace(-4, 4, 200)
plt.plot(x, np.arctan(x)/np.pi + 0.5, 'r')
plt.show()

# %% Exercice 3 — Polya
R = Polya(500, 1, 1)
X_frac = R / (2 + np.arange(501))
Y_frac = 1 - X_frac
Z_frac = X_frac / Y_frac
plt.figure()
plt.plot(X_frac, 'r', label='X')
plt.plot(Y_frac, label='Y')
plt.plot(Z_frac, 'g', label='Z')
plt.legend(); plt.show()

# %% 4
plt.figure()
X = Polyaloi(500, 500, 1, 1)
_plotrep_local(X)
plt.title('Polyaloi(1,1) — converge vers U[0,1]')
plt.show()

plt.figure()
X = Polyaloi(500, 500, 4, 6)
_plotrep_local(X)
plt.show()

# %% 5a — Urne n=4, discrete uniform on {1,...,5}
R_arr = np.zeros(3000, dtype=int)
for k in range(3000):
    val = 1
    for l in range(1, 5):
        val = int(Urne(val, l-1, 1, 1))
    R_arr[k] = val
plt.figure()
w = np.ones(3000) / 3000
plt.hist(R_arr, bins=np.arange(0.5, 6.5), weights=w)
plt.show()
plt.figure()
_plotrep_local(R_arr)
plt.step(np.arange(1, 6), np.arange(1, 6)/5, 'r', where='post')
plt.show()

# %% 6 — Beta distributions
for r_val, b_val, F_str in [(2, 1, lambda t: t**2),
                             (5, 1, lambda t: t**5),
                             (2, 2, lambda t: 3*t**2 - 2*t**3),
                             (2, 5, lambda t: 30*(t**2/2 - 4*t**3/3 + 3*t**4/2 - 4*t**5/5 + t**6/6))]:
    plt.figure()
    X = Polyaloi(500, 500, r_val, b_val)
    _plotrep_local(X)
    x = np.linspace(0, 1, 200)
    plt.plot(x, F_str(x), 'r')
    plt.title(f'Polyaloi r={r_val}, b={b_val}')
    plt.show()

# %% Exercice 4 — Ehrenfest
Bin = binom_dist.pmf(np.arange(6), 5, 0.5)

X = np.zeros(100, dtype=int)
for k in range(99):
    X[k+1] = int(Ehrenfest(X[k], 5))
plt.figure(); plt.plot(X); plt.title('Ehrenfest 100 steps'); plt.show()

X = np.zeros(5000, dtype=int)
for k in range(4999):
    X[k+1] = int(Ehrenfest(X[k], 5))

fig, axes = plt.subplots(2, 3)
for m in range(6):
    ax = axes[m//3, m%3]
    Erg = np.cumsum(X == m) / np.arange(1, 5001)
    ax.plot(Erg); ax.axhline(Bin[m], color='r'); ax.set_title(f'm={m}')
plt.tight_layout(); plt.show()

# Modified chain (lazy / aperiodic)
P_mat = np.array([[0, 1, 0, 0, 0, 0],
                   [1/5, 0, 4/5, 0, 0, 0],
                   [0, 2/5, 0, 3/5, 0, 0],
                   [0, 0, 3/5, 0, 2/5, 0],
                   [0, 0, 0, 4/5, 0, 1/5],
                   [0, 0, 0, 0, 1, 0]])
P_lazy = (5/6) * P_mat + (1/6) * np.eye(6)
Bin2 = binom_dist.pmf(np.arange(6), 5, 0.5)
print('Invariant check:', Bin2 @ P_lazy)

X = np.zeros(5000, dtype=int)
for k in range(4999):
    X[k+1] = int(Ehrenfest2(X[k], 5))

fig, axes = plt.subplots(2, 3)
for m in range(6):
    ax = axes[m//3, m%3]
    Erg = np.cumsum(X == m) / np.arange(1, 5001)
    ax.plot(Erg); ax.axhline(Bin2[m], color='r'); ax.set_title(f'm={m}')
plt.tight_layout(); plt.show()
