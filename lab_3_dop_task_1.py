import numpy as np

n = int(input())
m = int(input())
kk, ll, gg = np.zeros((n, m))

for i in range(n):
    for j in range(m):
        kk[i, j] = int(input())

for i in range(n):
    for j in range(m):
        gg[i, j] = int(input())

for i in range(n):
    for j in range(m):
        if kk[i, j] > gg[i, j]:
            kk[i, j] = ll[i, j]
        else:
            gg[i, j] = ll[i, j]

print(ll)