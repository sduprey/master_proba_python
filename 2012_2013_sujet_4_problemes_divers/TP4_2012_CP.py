"""TP4 2012-2013 Correction — Markov, IC, sondage."""
import numpy as np
import matplotlib.pyplot as plt

from plotrep import plotrep
from Markov import Markov
from Intconf import Intconf
from Intconfp import Intconfp
from sondage import sondage

# %% 1. Chaîne de Markov — loi stationnaire
A = np.array([[0, 1/3, 2/3], [1/3, 0, 2/3], [2/3, 1/3, 0]])
P_vec = np.array([0.35, 0.25, 0.4])
print(P_vec @ A)

p0 = np.array([0.05, 0.9, 0.05])
for n in [5, 10, 50, 100]:
    print(f'p{n} =', p0 @ np.linalg.matrix_power(A, n))

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
plt.step(np.arange(1, 4), np.cumsum(P_vec), 'r', where='post')
plt.title('Loi stationnaire chaîne de Markov')
plt.show()

# %% 2. Intervalles de confiance
X = np.random.randn(1000)
print('IC (sigma inconnu):', Intconf(X, np.std(X, ddof=1), 0.05))

k = 0
for i in range(20):
    X = np.random.randn(1000)
    Ic = Intconf(X, np.std(X, ddof=1), 0.05)
    if 0 > Ic[0] and 0 < Ic[1]:
        k += 1
print(f'k = {k}  (suit approx. Binomiale(20, 0.9))')

X = np.random.randn(1000)
a_vec = np.arange(0.01, 1.0, 0.01)
I1 = np.zeros(len(a_vec))
I2 = np.zeros(len(a_vec))
for i, ai in enumerate(a_vec):
    Ic = Intconf(X, np.std(X, ddof=1), ai)
    I1[i] = Ic[0]; I2[i] = Ic[1]
plt.figure()
plt.plot(a_vec, I1); plt.plot(a_vec, I2)
plt.xlabel('alpha'); plt.title('IC en fonction de alpha')
plt.show()

# %% 3. Intervalles de confiance pour une proportion
print('IC proportion (100, 64):', Intconfp(100, 64, 0.05))
print('IC proportion (400, 212):', Intconfp(400, 212, 0.05))

print('sondage(400, 212):', sondage(400, 212))
print('sondage(100, 52):', sondage(100, 52))
print('sondage(100, 60):', sondage(100, 60))
