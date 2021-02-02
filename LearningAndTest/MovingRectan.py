# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, 2*np.pi, 240)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
point_ani = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='red', alpha=0.3)
ax.add_patch(point_ani)

plt.grid(ls='--')
def update_points(num):
    """
    更新数据点，num代表当前帧的帧数
    """
    point_ani.set_x(x[num])
    return point_ani,

ani = animation.FuncAnimation(fig, update_points, np.arange(0, 240), interval=0, blit=True)
ani.save('sin_test2.gif', fps=240)