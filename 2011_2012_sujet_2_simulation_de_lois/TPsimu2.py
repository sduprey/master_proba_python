"""TP Simulation 2 — 2011-2012 (suite)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from plotrep import plotrep
from runif import runif
from rexp import rexp
from mystere import mystere

# %% 14. Exponential via CDF inversion
E = rexp(1000, 2)
print(np.mean(E))
plt.figure()
plt.hist(E, bins=20, density=True)
x = np.linspace(0, 4, 200)
plt.plot(x, 2 * np.exp(-2 * x))
plt.show()
plt.figure()
plotrep(E)
plt.plot(x, 1 - np.exp(-2 * x), 'r')
plt.show()

# %% 16. Geometric — mystere(p) generates Geometric(p)
geom = np.array([mystere(1/6) for _ in range(1000)])
print(np.mean(geom))
w = np.ones(1000) / 1000
xg = np.arange(1, 41)
plt.figure()
plt.hist(geom, bins=np.arange(0.5, max(geom)+1.5), weights=w)
plt.stem(xg, 1/6 * (5/6)**(xg - 1), 'r', markerfmt='ro', basefmt=' ')
plt.show()

# %% 17. Normal(10, 5)
Xn = 10 + np.random.randn(1000) * 5
plt.figure()
plt.hist(Xn, bins=20, density=True)
x = np.linspace(-10, 30, 200)
plt.plot(x, norm.pdf(x, 10, 5), 'r')
plt.show()
# Alternative
plt.figure()
plt.hist(Xn, bins=20, density=True)
plt.plot(x, norm.pdf(x, 10, 5), 'r')
plt.show()

# %% 18. Monte Carlo disk
X = 2 * np.random.rand(10000) - 1
Y = 2 * np.random.rand(10000) - 1
I = np.where(X**2 + Y**2 < 1)[0]
Xd, Yd = X[I], Y[I]
plt.figure()
plt.plot(Xd, Yd, 'd', ms=1)
t = np.linspace(0, 2*np.pi, 200)
plt.plot(np.cos(t), np.sin(t), 'r')
plt.axis('equal')
plt.show()

plt.figure(); plt.hist(Xd, bins=15, density=True); plt.title('Xd not uniform'); plt.show()

# %% Non-uniform polar sampling
r = np.random.rand(10000)
t2 = 2 * np.pi * np.random.rand(10000)
plt.figure()
plt.plot(r * np.cos(t2), r * np.sin(t2), '.', ms=1)
plt.show()

# %% Cardioid rejection
Abs1 = runif(10000, -1/4, 2)
Ord1 = runif(10000, -3*np.sqrt(3)/4, 3*np.sqrt(3)/4)
R = np.sqrt(Abs1**2 + Ord1**2)
T = np.arctan2(Ord1, Abs1)
I = np.where(R - np.cos(T) < 1)[0]
Cardx, Cardy = Abs1[I], Ord1[I]
plt.figure()
plt.plot(Cardx, Cardy, 'd', ms=1)
t3 = np.linspace(0, 2*np.pi, 200)
plt.plot((1+np.cos(t3))*np.cos(t3), (1+np.cos(t3))*np.sin(t3), 'r')
plt.show()
