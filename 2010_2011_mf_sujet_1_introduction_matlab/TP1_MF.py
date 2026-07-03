"""TP1 Master Maths Fondamentales — Introduction à Python (NumPy/Matplotlib)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad
from scipy.optimize import fsolve

from toto import toto
from q12 import q12

# Variables
a = 4; b = np.pi
print(f'a={a}, b={b}')
del b
print(f'a={a}')
print(np.sqrt(a))

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A); print(A[1, 2])

X = np.arange(1, 21); print(X)
Y = np.arange(1, 21, 2); print(Y)
print(np.arange(1, -2.5, -0.5))

b_row = A[1, :]; c_col = A[:, 2]; B_sub = A[0:2, 0:2]; C_sub = A[:, 0:2]

print(A.shape[0])
C = A.T
print(A + C); print(A @ C)

n = 4
I4 = np.eye(n); B = np.zeros((n, n)); D = np.ones((n, n))
print(np.linalg.matrix_power(A, 2))
print(np.linalg.det(A), np.trace(A), np.linalg.eig(A)[0])

E = 5 * np.ones((3, 3))
print(A[:, 0] @ A[:, 1])   # A(:,1)'*A(:,2)
print(A > 2)
rca = np.sqrt(np.arange(2, 12, 2))
print(A**2); print(A * C)

V = np.arange(1, 11)**2
W = 1 / np.arange(1, 11)

# Hilbert matrix
M = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        M[i, j] = 1 / (i + j + 1)
print(M); print(np.linalg.det(M)); print(np.linalg.inv(M)); print(np.linalg.eig(M)[0])

# Plots
t = np.arange(0, 3.1, 0.1)
plt.figure(); plt.plot(t, np.exp(t) + 3); plt.show()
plt.figure(); plt.plot(t, np.exp(t), t, 1 + t); plt.show()

# %% 11
plt.figure()
plt.plot(t, np.cos(t), t, np.sin(t), t, t**2)
plt.show()

x_pi = np.linspace(-np.pi, np.pi, 200)
plt.figure()
plt.plot(x_pi, np.cos(x_pi)); plt.plot(x_pi, np.sin(x_pi)); plt.plot(x_pi, x_pi**2)
plt.show()

# Functions
print(toto(2))
x01 = np.linspace(-1, 1, 200)
plt.figure(); plt.plot(x01, toto(x01)); plt.show()

result, _ = quad(toto, 0, 1); print(result)
root = fsolve(toto, 0)[0]; print(root)

# %% 12
plt.figure(); plt.plot(np.linspace(0, 1, 200), q12(np.linspace(0, 1, 200))); plt.show()
result12, _ = quad(q12, 0, 1); print(result12)
print(np.pi / 2 - 1)

toto2 = lambda x: np.cos(x)**2 - np.sin(x)**2
result2, _ = quad(toto2, 0, np.pi); print(result2)
root2 = fsolve(lambda x: x**3 - 3, 0)[0]; print(root2)

# %% 13
root3 = fsolve(lambda x: np.exp(x) - 3*x, 0)[0]; print(root3)

# %% Statistics
X = np.random.rand(1000)
s = np.sum(X); m = np.mean(X); v = np.var(X, ddof=1); sigma = np.std(X, ddof=1)
print(f's={s}, m={m}, v={v}, sigma={sigma}')

# %% 14
print(np.mean(X**3))

# %% Histograms
X = np.random.rand(100)
plt.figure(); plt.hist(X); plt.show()

X = np.random.rand(1000)
plt.figure(); plt.hist(X); plt.show()

X = np.random.rand(10000)
plt.figure(); plt.hist(X, bins=100, density=True); plt.show()
plt.figure(); plt.hist(X, bins=20, density=True); plt.show()

# %% 16 — Normal
X = np.random.randn(1000)
plt.figure()
plt.hist(X, bins=20, density=True)
x = np.linspace(-3, 3, 200)
plt.plot(x, norm.pdf(x), 'r')
plt.show()
print(np.mean(X), np.std(X, ddof=1))
