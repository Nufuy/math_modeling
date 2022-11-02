import numpy as np

n = 10
m = 15

a = np.zeros((n, m))

for i in range(n):
    for(j) in range(m):
        if i == 0 and j == 0:
            a[i, j] = np.sin(n * i + m * j)
        else:
            a[i, j] = np.sin(n * (i + 1) + (m * j))

print(a)
            