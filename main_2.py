import numpy as np

n = int(input())
a = [int(input()) for i in range(n)]

def my_funciya():
    c = 0
    for i in range(n):
        c += a[i]
    return c / n
print(my_funciya())