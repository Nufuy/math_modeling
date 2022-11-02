import numpy as np

n = int(input('chislo na kotoroe menyaem:'))
a = [int(input('chisla massiva:')) for i in range(5)]
m = int(input('mesto v massive:'))
a[m] = n
print(a)
