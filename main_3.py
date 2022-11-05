import numpy as np

n = int(input())
a = [int(input()) for i in range(n)]

def my_funciya():
    x = 1
    for i in range(n):
       x *= a[i]
    return x
print(my_funciya())