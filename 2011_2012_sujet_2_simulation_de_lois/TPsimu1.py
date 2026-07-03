"""TP Simulation 1 — 2011-2012."""
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

# %% 1. Normal
X = np.random.randn(1000)
plt.figure()
plt.hist(X, bins=20, density=True)
x = np.linspace(-3, 3, 200)
plt.plot(x, norm.pdf(x), 'r')
plt.show()
print(np.mean(X), np.std(X, ddof=1))

# %% 2. Binomial
Xbinom = np.random.binomial(10, 0.3, 1000)
print(np.mean(Xbinom), 10*0.3)
print(np.std(Xbinom, ddof=1), np.sqrt(10*0.3*0.7))
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
print(np.mean(Xpoi), np.std(Xpoi, ddof=1))
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
plt.plot(x, norm.cdf(x), 'r')
plt.show()
plotrep(Xn); plt.show()

# %% 6. Continuous uniforms
X = np.random.rand(1000)
for X_var in [np.random.rand(1000)+1, 2*np.random.rand(1000), 2*np.random.rand(1000)-1]:
    plt.figure(); plt.hist(X_var); plt.show()

XU4 = runif(1000, -3, 4)
plt.figure(); plt.hist(XU4); plt.show()

# %% 9. Bernoulli(0.5)
Pilface = (X < 0.5).astype(int)
plt.figure(); plt.hist(Pilface); plt.show()
print(np.mean(Pilface))

# %% 10. Bernoulli(p)
Ber = rbernou(1000, 1, 1/5).flatten()
plt.figure(); plt.hist(Ber); plt.show()

# %% 11. Uniform {1,...,10}
D = np.ceil(10 * np.random.rand(1000)).astype(int)
w = np.ones(1000) / 1000
plt.figure(); plt.hist(D, bins=np.arange(0.5, 11.5), weights=w); plt.show()
print(np.mean(D))

# %% 12. Dice
De = runifd(1000, 6)
w = np.ones(1000) / 1000
plt.figure(); plt.hist(De, bins=np.arange(0.5, 7.5), weights=w); plt.show()

# %% 13. Discrete distributions
Xd1 = discrete1(1000)
w = np.ones(1000) / 1000
plt.figure(); plt.hist(Xd1, bins=np.arange(0.5, 4.5), weights=w); plt.show()
Xd2 = discrete2(1000, [0.3, 0.2, 0.4, 0.1])
plt.figure(); plt.hist(Xd2, bins=np.arange(0.5, 5.5), weights=w); plt.show()
