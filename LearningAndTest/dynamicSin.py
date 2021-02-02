import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, 2*np.pi, 240)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111)
p, = ax.plot(x, y)
plt.grid(ls='--')
def update(num):
    p.set_xdata(x[0:num])
    p.set_ydata(y[0:num])
    return p,

ani = animation.FuncAnimation(fig, update, np.arange(0, 240), interval=0, blit=True)
ani.save('sin_dyn.gif', fps=240)
