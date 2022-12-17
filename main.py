import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1) # Пределы изменения переменной У
 
def update(frame): # Функция подстановки координат в объект анимации
    xdata.append(frame) # Рассщет координаты Х
    ydata.append(np.sin(frame)) # Рассщет координаты У
    anim_object.set_data(xdata, ydata) # Передача координат
    return anim_object,
 
ani = FuncAnimation(fig, # Стандартный вызов пространства для анимации
                    update, # Вызов функции подстановки координат
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=30 # Интервал между кадрами,
                    )

ani.save('lec_7_create_animation.gif')