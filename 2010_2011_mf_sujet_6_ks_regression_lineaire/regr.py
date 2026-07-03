import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t as t_dist, f as f_dist


def regr(Y, X):
    """Simple linear regression of Y on X with confidence intervals."""
    n = len(X)
    u = np.ones(n)
    M = np.column_stack([u, X])
    h = M.T @ M
    g = np.linalg.inv(h)
    droite = g @ M.T @ Y
    s = np.linalg.norm(Y - M @ droite) / np.sqrt(n - 2)

    t_crit = t_dist.ppf(0.975, n - 2)
    eca = np.sqrt(g[0, 0]) * s
    Ica = np.array([droite[0] - eca * t_crit, droite[0] + eca * t_crit])
    ecb = np.sqrt(g[1, 1]) * s
    Icb = np.array([droite[1] - ecb * t_crit, droite[1] + ecb * t_crit])

    print(f'droite = {droite}')
    print(f's = {s}')
    print(f'Ica = {Ica}')
    print(f'Icb = {Icb}')

    plt.figure()
    plt.plot(X, Y, 'o')
    plt.plot(X, droite[0] * u + droite[1] * X, 'r', label='regression')
    plt.plot(X, Ica[0] * u + Icb[0] * X, 'g')
    plt.plot(X, Ica[1] * u + Icb[1] * X, 'm')
    plt.legend()

    # Confidence ellipse for (a, b)
    plt.figure()
    A = h[0, 0]; B = h[1, 1]; C = 2 * h[0, 1]
    D = 2 * s**2 * f_dist.ppf(0.975, 2, n - 2)
    t_arr = np.linspace(0, 2 * np.pi, 301)
    r = np.sqrt(D / (A * np.cos(t_arr)**2 + B * np.sin(t_arr)**2 + C * np.cos(t_arr) * np.sin(t_arr)))
    plt.plot(droite[0] + r * np.cos(t_arr), droite[1] + r * np.sin(t_arr))

    return droite, s, Ica, Icb
