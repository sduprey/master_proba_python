import numpy as np

M = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        M[i, j] = 1 / (i + j + 1)

print(M)
print(np.linalg.det(M))
print(np.linalg.inv(M))
print(np.linalg.eig(M)[0])
