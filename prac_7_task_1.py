import numpy as np
import matplotlib.pyplot as plt

def ast(R):
  t = np.arange(-100, 100, 0.1)
  x = R * np.cos(t)**3
  y = R * np.sin(t)**3
  plt.plot(x, y, color='b', label='astroid')
  plt.grid()
  plt.axis('equal')
  plt.show() 


def cicl(R):
  t = np.arange(-100, 100, 0.1)
  x = R * (t - np.sin(t))
  y = R * (1 - np.cos(t))
  plt.plot(x, y, color='b', label='cilcoid')
  plt.grid()
  plt.axis('equal')
  plt.show()

cicl(10)

ast(10)
