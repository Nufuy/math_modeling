import matplotlib.pyplot as plt
import numpy as np

def elips(a , b, xa, xb, N):
    x = np.arange(xa, xb, N)
    y = np.arange(xa, xb, N)

    X, Y = np.meshgrid(x,y)

    fxy = (X**2/a**2)+(Y**2/b**2)
    plt.contour(X, Y, fxy, levels=[110])
    plt.axis('equal')                               # не учитывать разрешение экрана
    plt.savefig('pic_33.png')

elips(8, 4, -130, 130, 0.1)