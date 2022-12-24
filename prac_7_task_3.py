import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
xdata, ydata = [], []

ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)

def 