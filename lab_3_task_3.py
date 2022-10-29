import numpy as np
y0 = 0
x0 = 0
v = 15
alpha = 30
vx0 = v * np.sin(np.pi / 180 * alpha)
vy0 = v * np.cos(np.pi / 180 * alpha)

t = np.arange(0, 5, 0.001)
x = x0 + vx0 * t
y = y0 + vy0 * t - g * t ** 2 / 2

coords_time = np.zeros((len(t), 3))
for i in range(len(t)):
    coords_time[i, 0] = t[i]
    coords_time[i, 1] = x[i]
    coords_time[i, 2] = y[i]

print(coords_time)