import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad
from scipy.optimize import fsolve

from me import me
from toto import toto
from q10 import q10

# %% Variables and matrices
a = 4
b = np.pi
print(f'a={a}, b={b}')
del b
print(f'a={a}')
print(np.sqrt(a))

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
print(A[1, 2])  # A(2,3) in MATLAB

# %% Use of ranges (arange)
X = np.arange(1, 21)
print(X)
Y = np.arange(1, 21, 2)
print(Y)
print(np.arange(1, -2.5, -0.5))

# Operations on matrices
b = A[1, :]     # A(2,:)
c = A[:, 2]     # A(:,3)
B = A[0:2, 0:2] # A(1:2,1:2)
C = A[:, 0:2]   # A(:,1:2)

print(A.shape[0])        # length(A) — max dimension
C = A.T
print(A + C)
print(A @ C)             # matrix multiply

n = 4
I4 = np.eye(n)
B = np.zeros((n, n))
C = np.ones((n, n))
print(np.linalg.matrix_power(A, 2))

E = 5 * np.ones((3, 3))
print(A > 2)
rca = np.sqrt(np.arange(2, 12, 2))
print(A @ A)         # matrix power
print(A**2)          # elementwise power
print(A @ C)
print(A * C)         # elementwise multiply

# %% Vectors
V = np.arange(1, 11)**2
V2 = 1 / np.arange(1, 11)

# %% Loops — Hilbert matrix (see matTP1.py)
M = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        M[i, j] = 1 / (i + j + 1)
print(M)
print(np.linalg.det(M))
print(np.linalg.inv(M))
print(np.linalg.eig(M)[0])

# %% Plots
t = np.arange(0, 3.1, 0.1)
plt.figure(); plt.plot(t, np.exp(t) + 3); plt.show()

plt.figure(); plt.plot(t, np.exp(t), t, 1 + t); plt.show()

# %% 10
plt.figure()
plt.plot(t, np.cos(t), t, np.sin(t), t, t**2)
plt.show()

x_pi = np.linspace(-np.pi, np.pi, 200)
plt.figure()
plt.plot(x_pi, np.cos(x_pi))
plt.plot(x_pi, np.sin(x_pi))
plt.plot(x_pi, x_pi**2)
plt.show()

# %% Functions
print(toto(2))
x_01 = np.linspace(-1, 1, 200)
plt.figure(); plt.plot(x_01, toto(x_01)); plt.show()

result, _ = quad(toto, 0, 1)
print(result)
root = fsolve(toto, 0)[0]
print(root)

# %% 11
x_01 = np.linspace(0, 1, 200)
plt.figure(); plt.plot(x_01, q10(x_01)); plt.show()
result, _ = quad(q10, 0, 1)
print(result)
print(np.pi / 2 - 1)

toto2 = lambda x: np.cos(x)**2 - np.sin(x)**2
result2, _ = quad(toto2, 0, np.pi)
print(result2)
root2 = fsolve(lambda x: x**3 - 3, 0)[0]
print(root2)

# %% 12
root3 = fsolve(lambda x: np.exp(x) - 3*x, 0)[0]
print(root3)

# %% Statistics
X = np.random.rand(1000)
s = np.sum(X)
m = np.mean(X)
v = np.var(X, ddof=1)
sigma = np.std(X, ddof=1)
print(f's={s}, m={m}, v={v}, sigma={sigma}')
print(np.std(X, ddof=0))  # std(X,1) in MATLAB

Z = (X - m) / sigma
print(np.mean(Z), np.std(Z, ddof=1))

W = np.cumsum(X)

# %% 13
print(np.mean(X**3))

# %% 14
moy, ec = me(X)
print(f'moy={moy}, ec={ec}')

# %% Histograms — 15
X = np.random.rand(100)
plt.figure(); plt.hist(X); plt.show()

X = np.random.rand(1000)
plt.figure(); plt.hist(X, bins=10, density=True); plt.show()

X = np.random.rand(1000)
w = np.ones(len(X)) / len(X)
plt.figure(); plt.hist(X, bins=10, weights=w); plt.show()

X = np.random.rand(10000)
plt.figure(); plt.hist(X, bins=20, density=True); plt.show()

# %% 16
X = np.random.randn(1000)
plt.figure()
plt.hist(X, bins=20, density=True)
x = np.linspace(-3, 3, 200)
plt.plot(x, norm.pdf(x), 'r')
plt.show()
print(me(X))

# %% 17 — binomial (uses scipy)
from scipy.stats import binom as binom_dist
Xbinom = np.random.binomial(10, 0.3, 1000)
plt.figure()
w = np.ones(len(Xbinom)) / len(Xbinom)
plt.hist(Xbinom, bins=np.arange(-0.5, 11.5), weights=w)
k = np.arange(11)
plt.stem(k, binom_dist.pmf(k, 10, 0.3), 'r', markerfmt='ro', basefmt=' ')
m_b, s_b = me(Xbinom)
print(f'm={m_b}, s={s_b}')
plt.show()

# %% 18 — exponential
Xexp = np.random.exponential(0.5, 1000)  # rate=2 -> scale=0.5
m_e, s_e = me(Xexp)
print(f'm={m_e}, s={s_e}')
plt.figure()
plt.hist(Xexp, bins=20, density=True)
x = np.linspace(0, 3, 200)
plt.plot(x, 2 * np.exp(-2 * x))
plt.show()

# %% 18 — Poisson
from scipy.stats import poisson
Xpoi = np.random.poisson(2, 1000)
m_p, s_p = me(Xpoi)
print(f'm={m_p}, s={s_p}')
k = np.arange(11)
ppois = np.exp(-2) * 2**k / np.array([np.math.factorial(ki) for ki in k])
plt.figure()
w = np.ones(len(Xpoi)) / len(Xpoi)
plt.hist(Xpoi, bins=np.arange(-0.5, max(Xpoi) + 1.5), weights=w)
plt.stem(k, ppois, 'r', markerfmt='ro', basefmt=' ')
plt.show()
