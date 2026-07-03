"""TP2 2012-2013 — Simulation de lois."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom as binom_dist

from plotrep import plotrep
from runif import runif
from rbernou import rbernou
from runifd import runifd
from discrete1 import discrete1
from discrete2 import discrete2
from rexp import rexp
from mystere import mystere

# %% 1. Normal
X = np.random.randn(1000)
plt.figure()
plt.hist(X, bins=20, density=True)
x = np.linspace(-3, 3, 200)
plt.plot(x, norm.pdf(x), 'r')
plt.show()
print(np.mean(X), np.std(X, ddof=1))

# %% 4. Normal empirical CDF
Xn = np.random.randn(1000)
Y = np.sort(Xn)
plt.figure()
plt.step(Y, np.arange(1, 1001)/1000, where='post')
plt.plot(x, norm.cdf(x), 'r')
plt.show()
plotrep(Xn); plt.show()

# %% Binomial CDF
Z = np.random.binomial(10, 0.3, 1000)
print(np.mean(Z), np.std(Z, ddof=1))
plt.figure()
plotrep(Z)
k = np.arange(11)
plt.step(k, binom_dist.cdf(k, 10, 0.3), where='post')
plt.show()

# %% 6. Continuous uniforms
X = np.random.rand(1000)
for X_var in [np.random.rand(1000)+1, 2*np.random.rand(1000), 2*np.random.rand(1000)-1]:
    plt.figure(); plt.hist(X_var); plt.show()

XU4 = runif(1000, -3, 4)
plt.figure(); plt.hist(XU4); plt.show()

# %% 8. Bernoulli(0.3)
Pilface = (X < 0.3).astype(int)
plt.figure(); plt.hist(Pilface); plt.show()
print(np.mean(Pilface))

# %% 9. Bernoulli(p)
Ber = rbernou(1000, 1/5)
plt.figure(); plt.hist(Ber); plt.show()

# %% 10. Uniform {1,...,10}
D = np.ceil(10 * np.random.rand(1000)).astype(int)
w = np.ones(1000) / 1000
plt.figure(); plt.hist(D, bins=np.arange(0.5, 11.5), weights=w); plt.show()
print(np.mean(D))

# %% 11. Dice
De = runifd(1000, 6)
w = np.ones(1000) / 1000
plt.figure(); plt.hist(De, bins=np.arange(0.5, 7.5), weights=w); plt.show()

# %% 12. Discrete {1,2,3}
Xd1 = discrete1(1000)
w = np.ones(1000) / 1000
plt.figure(); plt.hist(Xd1, bins=np.arange(0.5, 4.5), weights=w); plt.show()

# %% 13. General discrete
Xd2 = discrete2(1000, [0.3, 0.2, 0.4, 0.1])
plt.figure(); plt.hist(Xd2, bins=np.arange(0.5, 5.5), weights=w); plt.show()

# %% Exponential
E = rexp(1000, 2)
print(np.mean(E))
plt.figure()
plt.hist(E, bins=20, density=True)
x2 = np.linspace(0, 4, 200)
plt.plot(x2, 2 * np.exp(-2 * x2))
plt.show()
plt.figure()
plotrep(E)
plt.plot(x2, 1 - np.exp(-2 * x2), 'r')
plt.show()

# %% Cauchy (local inversion)
X_c = np.random.rand(1000)
X_cauchy = -np.tan(np.pi * (X_c - 0.5))
plotrep(X_cauchy)
x_c = np.linspace(-15, 15, 200)
plt.plot(x_c, 1/np.pi * (np.arctan(x_c) + np.pi/2), 'r')
plt.show()

# %% 16. Geometric — mystere(p)
geom = np.array([mystere(1/6) for _ in range(1000)])
print(np.mean(geom))

# %% 18. Disk rejection
X_d = 2 * np.random.rand(10000) - 1
Y_d = 2 * np.random.rand(10000) - 1
I = np.where(X_d**2 + Y_d**2 < 1)[0]
Xd, Yd = X_d[I], Y_d[I]
plt.figure()
plt.plot(Xd, Yd, 'd', ms=1)
t = np.linspace(0, 2*np.pi, 200)
plt.plot(np.cos(t), np.sin(t), 'r')
plt.axis('equal'); plt.show()

plt.figure(); plt.hist(Xd, bins=15, density=True); plt.show()

# Radial distribution
plt.figure(); plt.hist(np.sqrt(Xd**2 + Yd**2), bins=15, density=True); plt.show()
plt.figure()
plotrep(np.sqrt(Xd**2 + Yd**2))
xr = np.linspace(0, 1, 200)
plt.plot(xr, xr**2, 'r')
plt.show()

# %% 19. Non-uniform polar
r = np.random.rand(10000)
t2 = 2 * np.pi * np.random.rand(10000)
plt.figure(); plt.plot(r*np.cos(t2), r*np.sin(t2), '.', ms=1); plt.show()

# %% 20. Cardioid
Abs1 = runif(10000, -1/4, 2)
Ord1 = runif(10000, -3*np.sqrt(3)/4, 3*np.sqrt(3)/4)
R_c = np.sqrt(Abs1**2 + Ord1**2)
T_c = np.arctan2(Ord1, Abs1)
I_c = np.where(R_c - np.cos(T_c) < 1)[0]
plt.figure()
plt.plot(Abs1[I_c], Ord1[I_c], 'd', ms=1)
t3 = np.linspace(0, 2*np.pi, 200)
plt.plot((1+np.cos(t3))*np.cos(t3), (1+np.cos(t3))*np.sin(t3), 'r')
plt.show()
