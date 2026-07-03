"""TP2 Master Maths Fondamentales — Simulation de lois."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom as binom_dist

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '2010_2011_sujet_2_simulation_de_lois'))

from plotrep import plotrep
from runif import runif
from rbernou import rbernou
from runifd import runifd
from discrete1 import discrete1
from discrete2 import discrete2
from rcauchy import rcauchy

# %% 1. Normal
X = np.random.randn(1000)
plt.figure()
plt.hist(X, bins=20, density=True)
x = np.linspace(-3, 3, 200)
plt.plot(x, norm.pdf(x), 'r')
plt.show()
m, e = np.mean(X), np.std(X, ddof=1)
print(f'm={m}, e={e}')

# %% 3. Normal empirical CDF
Xn = np.random.randn(1000)
Y = np.sort(Xn)
plt.figure()
plt.step(Y, np.arange(1, 1001)/1000, where='post')
plt.plot(x, norm.cdf(x), 'r')
plt.show()

plotrep(Xn); plt.show()

# %% 5. Continuous uniforms
X = np.random.rand(1000)
for X_var in [X + 1, 2*X, 2*X - 1]:
    plt.figure(); plt.hist(X_var); plt.show()

XU4 = runif(1000, -3, 4)
plt.figure(); plt.hist(XU4); plt.show()

# %% 7. Bernoulli(0.5)
Pilface = (X < 0.5).astype(int)
plt.figure(); plt.hist(Pilface); plt.show()
print(np.mean(Pilface))

# %% 8. Bernoulli(p) — note: rbernou(1, n, p) in original → rbernou(n, 1, p)
Ber = rbernou(1000, 1, 1/5).flatten()
plt.figure(); plt.hist(Ber); plt.show()

# %% 9. Uniform {1,...,10}
D = np.ceil(10 * np.random.rand(1000)).astype(int)
w = np.ones(1000) / 1000
plt.figure()
plt.hist(D, bins=np.arange(0.5, 11.5), weights=w)
plt.step(np.arange(1, 12), np.ones(11)/10, 'm', where='post')
plt.show()
print(np.mean(D))

# %% 10. Dice
De = runifd(1000, 6)
w = np.ones(1000) / 1000
plt.figure(); plt.hist(De, bins=np.arange(0.5, 7.5), weights=w); plt.show()

# %% 11. Discrete {1,2,3}
Xd1 = discrete1(1000)
w = np.ones(1000) / 1000
plt.figure(); plt.hist(Xd1, bins=np.arange(0.5, 4.5), weights=w); plt.show()

# %% 12. General discrete
Xd2 = discrete2(1000, [0.3, 0.2, 0.4, 0.1])
w = np.ones(1000) / 1000
plt.figure(); plt.hist(Xd2, bins=np.arange(0.5, 5.5), weights=w); plt.show()
