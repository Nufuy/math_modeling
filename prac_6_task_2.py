import matplotlib.pyplot as plt
import numpy as np

def para(a, b, c, xa, xb, N, title='parabola'):
    x = np.arange(xa, xb, N)
    y = a*x**2 + b*x + c
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.grid()
    plt.plot(x, y)
    plt.savefig('pic_22.png')


def giper(k, xa, xb, N, title='giperbola'):
    x = np.arange(xa, xb, N)
    y = k/x
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.grid()
    plt.plot(x, y)
    plt.savefig('pic_22--.png')

giper(1, 1, 10, 0.01)
