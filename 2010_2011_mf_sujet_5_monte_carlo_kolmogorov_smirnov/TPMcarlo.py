"""Monte Carlo et Kolmogorov-Smirnov — Master MF 2010-2011."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from Intconf import Intconf
from DKS import DKS

# %% Monte Carlo — estimation de pi
U = np.random.rand(500)
X = 4 * np.sqrt(1 - U**2)
print(f'mean={np.mean(X):.4f}, std={np.std(X, ddof=1):.4f}')
print(f'IC pi: {Intconf(X, np.std(X, ddof=1), 0.05)}')

# répéter 100 fois et compter les fois où pi est dans l'IC
N = 0
for k in range(100):
    U = np.random.rand(500)
    X = 4 * np.sqrt(1 - U**2)
    Ic = Intconf(X, np.std(X, ddof=1), 0.05)
    N += (np.pi > Ic[0]) and (np.pi < Ic[1])
print(f'N (should be ~95): {N}')

# %% Rejet — disque
U1 = np.random.rand(500); U2 = np.random.rand(500)
X = 4 * ((U1**2 + U2**2) < 1).astype(float)
print(f'mean={np.mean(X):.4f}')
s = np.sqrt(np.mean(X) * (4 - np.mean(X)))
print(f'IC pi (rejet): {Intconf(X, s, 0.05)}')

# %% Boule 3D
U1 = np.random.rand(500); U2 = np.random.rand(500); U3 = np.random.rand(500)
X = 6 * ((U1**2 + U2**2 + U3**2) < 1).astype(float)
print(f'Volume boule 3D ~ {np.mean(X):.4f}  (theorique = {4*np.pi/3:.4f})')
print(f'IC: {Intconf(X, np.std(X, ddof=1), 0.05)}')

# %% Intégrale (sphère 3D, x^2 component)
U1 = 2*np.random.rand(500)-1; U2 = 2*np.random.rand(500)-1; U3 = 2*np.random.rand(500)-1
X = 8 * U1**2 * ((U1**2 + U2**2 + U3**2) < 1).astype(float)
print(f'Intégrale ~ {np.mean(X):.4f}  (theorique = {4*np.pi/15:.4f})')
print(f'IC: {Intconf(X, np.std(X, ddof=1), 0.05)}')

# %% Kolmogorov-Smirnov — test d'adéquation
X = np.random.randn(100)
print('KS normal vs normal:', DKS(X, norm.cdf, 0.05))

X = np.random.rand(100)
print('KS uniforme vs normal:', DKS(X, norm.cdf, 0.05))
print('KS uniforme vs uniforme:', DKS(X, lambda x: x, 0.05))

rexp_samples = -np.log(np.random.rand(100))
print('KS exp vs exp CDF:', DKS(rexp_samples, lambda x: 1 - np.exp(-x), 0.05))

# %% IC puis KS avec les bornes
X = np.random.randn(1000)
Ic = Intconf(X, 1, 0.05)
print(f'IC moyenne: {Ic}')
print('KS avec borne basse:', DKS(X, lambda x: norm.cdf(x, Ic[0], 1), 0.05))
print('KS avec borne haute:', DKS(X, lambda x: norm.cdf(x, Ic[1], 1), 0.05))
