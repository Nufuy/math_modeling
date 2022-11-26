import matplotlib.pyplot as plt
import numpy as np

def parabola(a=1, b=1, c=0, title='parabola'):
    x = np.arange(-10, 10, 0.01)
    y = a*x**2 + b*x + c

    plt.plot(x, y, label='my parabola')
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.legend()
    plt.title('Base')
    plt.savefig('pic_3.png')

parabola()
