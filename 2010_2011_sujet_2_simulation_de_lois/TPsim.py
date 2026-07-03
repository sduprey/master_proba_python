"""Correction complète du TP simulation (2010-2011)."""
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

# %% 1. Normal histogram + density
X = np.random.randn(1000)
plt.figure()
plt.hist(X, bins=20, density=True)
x = np.linspace(-3, 3, 200)
plt.plot(x, norm.pdf(x), 'r')
plt.show()
m, e = np.mean(X), np.std(X, ddof=1)
print(f'm={m}, e={e}')

# %% 2. Binomial
Xbinom = np.random.binomial(10, 0.3, 1000)
m_b, s_b = np.mean(Xbinom), np.std(Xbinom, ddof=1)
print(f'm={m_b}, s={s_b}')
k = np.arange(11)
plt.figure()
w = np.ones(len(Xbinom)) / len(Xbinom)
plt.hist(Xbinom, bins=np.arange(-0.5, 11.5), weights=w)
plt.stem(k, binom_dist.pmf(k, 10, 0.3), 'r', markerfmt='ro', basefmt=' ')
plt.show()

plt.figure()
w = np.ones(len(Xbinom)) / len(Xbinom)
plt.hist(Xbinom, bins=np.arange(-0.5, max(Xbinom)+1.5), weights=w)
plt.show()

# %% 3. Poisson
Xpoi = np.random.poisson(2, 1000)
m_p, s_p = np.mean(Xpoi), np.std(Xpoi, ddof=1)
print(f'm={m_p}, s={s_p}')
val = np.arange(11)
ppois = np.exp(-2) * 2**val / np.array([np.math.factorial(v) for v in val])
plt.figure()
w = np.ones(len(Xpoi)) / len(Xpoi)
plt.hist(Xpoi, bins=np.arange(-0.5, max(Xpoi)+1.5), weights=w)
plt.stem(val, ppois, 'r', markerfmt='ro', basefmt=' ')
plt.show()

# %% 4. Normal empirical CDF
Xn = np.random.randn(1000)
Y = np.sort(Xn)
plt.figure()
plt.step(Y, np.arange(1, 1001)/1000, where='post')
x = np.linspace(-3, 3, 200)
plt.plot(x, norm.cdf(x), 'r')
plt.show()

plotrep(Xn)
plt.show()

# %% 6. Continuous uniforms
X = np.random.rand(1000)
XU = np.random.rand(1000) + 1
plt.figure(); plt.hist(XU); plt.show()
XU2 = 2 * np.random.rand(1000)
plt.figure(); plt.hist(XU2); plt.show()
XU3 = 2 * np.random.rand(1000) - 1
plt.figure(); plt.hist(XU3); plt.show()

XU4 = runif(1000, -3, 4)
plt.figure(); plt.hist(XU4); plt.show()

# %% 9. Bernoulli(0.5)
Pilface = (X < 0.5).astype(int)
plt.figure(); plt.hist(Pilface); plt.show()
print(np.mean(Pilface))

# %% 10. Bernoulli(p)
Ber = rbernou(1000, 1, 1/5).flatten()
plt.figure(); plt.hist(Ber); plt.show()

# %% 11. Discrete uniform {1,...,10}
D = np.ceil(10 * np.random.rand(1000)).astype(int)
w = np.ones(len(D)) / len(D)
plt.figure(); plt.hist(D, bins=np.arange(0.5, 11.5), weights=w); plt.show()
print(np.mean(D))

# %% 12. Dice
De = runifd(1000, 6)
w = np.ones(len(De)) / len(De)
plt.figure(); plt.hist(De, bins=np.arange(0.5, 7.5), weights=w); plt.show()

# %% 13. Discrete distributions
Xd1 = discrete1(1000)
w = np.ones(len(Xd1)) / len(Xd1)
plt.figure(); plt.hist(Xd1, bins=np.arange(0.5, 4.5), weights=w); plt.show()

Xd2 = discrete2(1000, [0.3, 0.2, 0.4, 0.1])
w = np.ones(len(Xd2)) / len(Xd2)
plt.figure(); plt.hist(Xd2, bins=np.arange(0.5, 5.5), weights=w); plt.show()

# %% 14. Exponential
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

# %% Geometric via loop
geom = np.zeros(1000, dtype=int)
for i in range(1000):
    j = 1
    while np.random.rand() > 1/6:
        j += 1
    geom[i] = j
print(np.mean(geom))
w = np.ones(len(geom)) / len(geom)
xg = np.arange(1, 41)
plt.figure()
plt.hist(geom, bins=np.arange(0.5, max(geom)+1.5), weights=w)
plt.stem(xg, 1/6 * (5/6)**(xg - 1), 'r', markerfmt='ro', basefmt=' ')
plt.show()

# %% Normal(10, 5)
Xn = 10 + np.random.randn(1000) * 5
plt.figure()
plt.hist(Xn, bins=20, density=True)
x = np.linspace(-10, 30, 200)
plt.plot(x, norm.pdf(x, 10, 5))
plt.show()

# %% Monte Carlo — uniform disk (pi estimation)
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

plt.figure()
plt.hist(Xd, bins=15, density=True)
plt.show()

# %% Random polar uniform (non-uniform!)
r = np.random.rand(10000)
t = 2 * np.pi * np.random.rand(10000)
plt.figure()
plt.plot(r * np.cos(t), r * np.sin(t), '.', ms=1)
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
t = np.linspace(0, 2*np.pi, 200)
plt.plot((1 + np.cos(t)) * np.cos(t), (1 + np.cos(t)) * np.sin(t), 'r')
plt.show()
