import matplotlib.pyplot as plt
import numpy as np

al = np.arange(-2*np.pi, 2*np.pi, 0.1)
R = 3

x = R * np.cos(al)
y = R * np.sin(al)

plt.plot(x, y, ls='--', lw=3)

plt.axis('equal')

plt.savefig('pic_5.png')
