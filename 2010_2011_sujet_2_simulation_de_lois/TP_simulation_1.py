import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom as binom_dist, poisson

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
plt.title('Normal density')
plt.show()
m, e = np.mean(X), np.std(X, ddof=1)
print(f'm={m}, e={e}')

# %% 2. Binomial histogram + PMF
Xbinom = np.random.binomial(10, 0.3, 1000)
m_b, s_b = np.mean(Xbinom), np.std(Xbinom, ddof=1)
print(f'm={m_b}, s={s_b}')
k = np.arange(11)
plt.figure()
w = np.ones(len(Xbinom)) / len(Xbinom)
plt.hist(Xbinom, bins=np.arange(-0.5, 11.5), weights=w)
plt.stem(k, binom_dist.pmf(k, 10, 0.3), 'r', markerfmt='ro', basefmt=' ')
plt.show()

# %% 3. Poisson histogram + PMF
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

# %% 4. Normal empirical CDF vs theoretical
Xn = np.random.randn(1000)
Y = np.sort(Xn)
plt.figure()
plt.step(Y, np.arange(1, 1001) / 1000, where='post')
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

# %% 8
XU4 = runif(1000, -3, 4)
plt.figure(); plt.hist(XU4); plt.show()

# %% 9. Bernoulli(0.5)
Pilface = X < 0.5
plt.figure(); plt.hist(Pilface); plt.show()
print(np.mean(Pilface))

# %% 10. Bernoulli(1/5)
Ber = X < (1/5)
plt.figure(); plt.hist(Ber); plt.show()

Ber = rbernou(1000, 1, 1/5).flatten()
plt.figure(); plt.hist(Ber); plt.show()

# %% 11. Discrete uniform on {1,...,10}
D = np.ceil(10 * np.random.rand(1000)).astype(int)
plt.figure()
w = np.ones(len(D)) / len(D)
plt.hist(D, bins=np.arange(0.5, 11.5), weights=w)
plt.show()
print(np.mean(D))

# %% 12. Dice roll
De = runifd(1000, 6)
plt.figure()
w = np.ones(len(De)) / len(De)
plt.hist(De, bins=np.arange(0.5, 7.5), weights=w)
plt.show()

# %% 13. Discrete law on {1,2,3}
Xd1 = discrete1(1000)
plt.figure()
w = np.ones(len(Xd1)) / len(Xd1)
plt.hist(Xd1, bins=np.arange(0.5, 4.5), weights=w)
plt.show()

# %% 13. General discrete law
Xd2 = discrete2(1000, [0.3, 0.2, 0.4, 0.1])
plt.figure()
w = np.ones(len(Xd2)) / len(Xd2)
plt.hist(Xd2, bins=np.arange(0.5, 5.5), weights=w)
plt.show()

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
