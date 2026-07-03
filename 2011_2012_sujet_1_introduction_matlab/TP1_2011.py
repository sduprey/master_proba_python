"""TP1 2011-2012 — Introduction à Python (NumPy/Matplotlib)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad
from scipy.optimize import fsolve


def toto(t):
    return t**2 - 3


def q10(x):
    return 2 / (1 + x**2) - 1


# Variables
a = 4; b = np.pi
print(f'a={a}, b={b}')
del b; print(f'a={a}'); print(np.sqrt(a))

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A); print(A[1, 2])

print(np.arange(1, 21))
print(np.arange(1, 21, 2))
print(np.arange(1, -2.5, -0.5))

b_row = A[1, :]; c_col = A[:, 2]; B_sub = A[0:2, 0:2]; C_sub = A[:, 0:2]
print(A.shape[0]); C = A.T; print(A + C); print(A @ C)

n = 4
I4 = np.eye(n); B = np.zeros((n, n)); Cones = np.ones((n, n))
print(np.linalg.matrix_power(A, 2))

E = 5 * np.ones((3, 3))
print(A > 2)
rca = np.sqrt(np.arange(2, 12, 2))
print(A**2); print(A * Cones)
V = np.arange(1, 11)**2; V2 = 1 / np.arange(1, 11)

# Hilbert matrix
M = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        M[i, j] = 1 / (i + j + 1)
print(M); print(np.linalg.det(M)); print(np.linalg.inv(M)); print(np.linalg.eig(M)[0])

# Plots
t = np.arange(0, 3.1, 0.1)
plt.figure(); plt.plot(t, np.exp(t) + 3, 'g'); plt.show()
plt.figure(); plt.plot(t, np.exp(t), t, 1 + t); plt.show()

# %% 9
plt.figure()
plt.plot(t, np.cos(t), t, np.sin(t), t, t**2)
plt.show()
x_pi = np.linspace(-np.pi, np.pi, 200)
plt.figure(); plt.plot(x_pi, np.cos(x_pi)); plt.plot(x_pi, np.sin(x_pi)); plt.plot(x_pi, x_pi**2); plt.show()

# Functions
print(toto(2))
x01 = np.linspace(-1, 1, 200)
plt.figure(); plt.plot(x01, toto(x01)); plt.show()
result, _ = quad(toto, 0, 1); print(result)
root = fsolve(toto, 1)[0]; print(root)

# %% 10
plt.figure(); plt.plot(np.linspace(0, 1, 200), q10(np.linspace(0, 1, 200))); plt.show()
result10, _ = quad(q10, 0, 1); print(result10); print(np.pi/2 - 1)

toto2 = lambda x: np.cos(x)**2 - np.sin(x)**2
result2, _ = quad(toto2, 0, np.pi); print(result2)
root2 = fsolve(lambda x: x**3 - 3, 2)[0]; print(root2)
root3 = fsolve(lambda x: np.exp(x) - 3*x, 0)[0]; print(root3)

# Statistics
X = np.random.rand(1000)
Y = np.random.rand(2, 3)
s = np.sum(X); m = np.mean(X); v = np.var(X, ddof=1); sigma = np.std(X, ddof=1)
print(f's={s}, m={m}, v={v}, sigma={sigma}')
print(np.std(X, ddof=0))

# %% 12
print(np.mean(X**3))

# Histograms
X100 = np.random.rand(100)
plt.figure(); plt.hist(X100); plt.show()

X1000 = np.random.rand(1000)
plt.figure(); plt.hist(X1000, bins=10, density=True); plt.show()
w = np.ones(len(X1000)) / len(X1000)
plt.figure(); plt.hist(X1000, bins=10, weights=w); plt.show()

X10k = np.random.rand(10000)
plt.figure(); plt.hist(X10k, bins=20, density=True); plt.show()

# %% 14 — Normal
Xn = np.random.randn(1000)
plt.figure()
plt.hist(Xn, bins=20, density=True)
x = np.linspace(-3, 3, 200)
plt.plot(x, norm.pdf(x), 'r')
plt.show()
print(np.mean(Xn), np.std(Xn, ddof=0))

# %% 15 — Binomial
from scipy.stats import binom as binom_dist
Xbinom = np.random.binomial(10, 0.3, 1000)
w = np.ones(len(Xbinom)) / len(Xbinom)
plt.figure()
plt.hist(Xbinom, bins=np.arange(-0.5, 11.5), weights=w)
k = np.arange(11)
plt.stem(k, binom_dist.pmf(k, 10, 0.3), 'r', markerfmt='ro', basefmt=' ')
print(np.mean(Xbinom), np.std(Xbinom, ddof=0))
plt.show()

# Exponential
Xexp = np.random.exponential(0.5, 1000)
print(np.mean(Xexp), np.std(Xexp, ddof=0))
plt.figure()
plt.hist(Xexp, bins=20, density=True)
x = np.linspace(0, 3, 200)
plt.plot(x, 2 * np.exp(-2 * x))
plt.show()

# Poisson
Xpoi = np.random.poisson(2, 1000)
print(np.mean(Xpoi), np.std(Xpoi, ddof=0))
k = np.arange(11)
ppois = np.exp(-2) * 2**k / np.array([np.math.factorial(ki) for ki in k])
w = np.ones(len(Xpoi)) / len(Xpoi)
plt.figure()
plt.hist(Xpoi, bins=np.arange(-0.5, max(Xpoi)+1.5), weights=w)
plt.stem(k, ppois, 'r', markerfmt='ro', basefmt=' ')
plt.show()
