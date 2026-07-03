"""TP Convergences de processus — Master MF 2010-2011."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom as binom_dist, norm

from Ehrenfest3 import Ehrenfest3
from Fattente import Fattente
from plotergo import plotergo
from convattente import convattente
from plotrep import plotrep

# %% Ehrenfest chain
X = np.zeros(500, dtype=int); X[0] = 1
for n in range(1, 500):
    X[n] = int(Ehrenfest3(5, X[n-1]))
plt.figure(); plt.plot(X); plt.title('Ehrenfest 500 steps'); plt.show()

# %% Convergence to binomial stationary distribution
Ehr900 = np.zeros(5000, dtype=int)
Ehr1000 = np.zeros(5000, dtype=int)
for k in range(5000):
    C = 1
    for n in range(1, 900):
        C = int(Ehrenfest3(5, C))
    Ehr900[k] = C
    for n in range(900, 1000):
        C = int(Ehrenfest3(5, C))
    Ehr1000[k] = C

plt.figure()
plotrep(Ehr900)
plotrep(Ehr1000)
k_arr = np.arange(6)
plt.step(k_arr, binom_dist.cdf(k_arr, 5, 0.5), 'r', where='post')
plt.show()

# %% Poisson process (exponential inter-arrivals)
inter = np.random.exponential(1, 500)
T = np.cumsum(inter)
plt.figure()
plt.step(T, np.arange(1, 501), where='post', label='N_t')
plt.plot(T, np.arange(1, 501) / T, 'r', label='N_t / t')
plt.axhline(1, color='k')
plt.legend(); plt.title('Poisson process'); plt.show()
Ic = np.array([500/np.sum(inter) - norm.ppf(0.975)*np.sqrt(500)/np.sum(inter),
               500/np.sum(inter) + norm.ppf(0.975)*np.sqrt(500)/np.sum(inter)])
print(f'IC taux: {Ic}')

# %% Minimum of uniforms → exponential
X = np.random.rand(500)
m_arr = np.zeros(500)
m_arr[0] = X[0]
for k in range(1, 500):
    m_arr[k] = min(X[k], m_arr[k-1])
plt.figure(); plt.plot(m_arr); plt.title('Running minimum → 0'); plt.show()

m_scaled = np.zeros(5000)
for k in range(5000):
    m_scaled[k] = 500 * np.min(np.random.rand(500))
plt.figure()
plotrep(m_scaled)
x = np.linspace(0, 3, 200)
plt.plot(x, 1 - np.exp(-x), 'r')
plt.title('500 * min(U_1,...,U_500) → Exp(1)'); plt.show()

# %% Queuing chain
X = np.zeros(1000, dtype=int)
plt.figure()
for (p, q, style) in [(0.1, 0.6, 'o'), (0.5, 0.5, 'r+'), (0.6, 0.1, 'g*')]:
    X[0] = 0
    for k in range(1, 1000):
        X[k] = Fattente(X[k-1], p, q)
    plt.plot(X, style, ms=3)
plt.title('File d\'attente'); plt.show()

# %% Ergodicity
plt.figure(); plotergo(0.1, 0.6, 10000); plt.suptitle('p=0.1, q=0.6 ergodique'); plt.show()
plt.figure(); plotergo(0.5, 0.55, 10000); plt.suptitle('p=0.5, q=0.55'); plt.show()

# %% Convergence in distribution
plt.figure(); convattente(0.1, 0.6); plt.title('p<q : converge'); plt.show()
plt.figure(); convattente(0.5, 0.5); plt.title('p=q : pas de convergence'); plt.show()
plt.figure(); convattente(0.6, 0.1); plt.title('p>q : pas de convergence'); plt.show()
