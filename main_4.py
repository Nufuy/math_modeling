import numpy as np
n = int(input())
a = [int(input()) for i in range(n)]

def my_funciya(a:list):
    c = 0
    for i in range(len(a)):
        c += a[i]
    return c / len(a)
print(my_funciya(a))
