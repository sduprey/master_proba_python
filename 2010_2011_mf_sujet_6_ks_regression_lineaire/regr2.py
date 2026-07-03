import numpy as np


def regr2(Y, MX):
    """Multiple linear regression of Y on columns of MX (intercept added automatically)."""
    n = len(Y)
    k = MX.shape[1]
    M2 = np.column_stack([np.ones(n), MX])
    g = np.linalg.inv(M2.T @ M2)
    bhat = g @ M2.T @ Y
    sigma = np.linalg.norm(Y - M2 @ bhat) / np.sqrt(n - k)
    print(f'bhat = {bhat}')
    print(f'sigma = {sigma}')
    return bhat, sigma
