import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], '--', color='b')
xdata, ydata = [], []

def cir(v, t):
    alpha = np.arange(0, 2 * np.pi, 0.1)
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    R = v * t
    return x, y

ed = 20
plt.axis('equal')
ax.set_xlim(-ed, ed)
ax.set_ylim(-ed, ed)

def animate(i):
  ball.set_data(cir(0.1, i))

ani = FuncAnimation(fig, animate, frames=100, interval=20)
ani.save('task_2.gif')