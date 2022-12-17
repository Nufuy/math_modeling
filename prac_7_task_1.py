import numpy as np
import matplotlib.pyplot as plt

def cicl(R):
    t = np.arange(-50, 50, 0.1)
    x = R * (t - np.sin(t))
    y = R * (t - np.cos(t))
    plt.plot(x, y, color='b')
    plt.grid()
    plt.axis('equal')
    plt.savefig('pic_11.png')

cicl(10)
