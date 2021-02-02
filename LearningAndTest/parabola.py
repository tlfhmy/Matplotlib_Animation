import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fp = 1200

p = 1.
y = np.linspace(-5., 5., fp)
x = y**2/(2.*p)

liney = np.linspace(-5., 5., fp)
linex = y*0-p/2.

fig = plt.figure(dpi=300)

ax = fig.add_subplot(111)
ax.plot(linex, liney)
ax.plot(p/2., 0, 'ro')
text_F = plt.text(p/2., 0, 'F', fontsize=16)


line1x = fig.add_subplot(111)
line2x = fig.add_subplot(111)
parabolax = fig.add_subplot(111)

temp1x = np.linspace(-p/2., x[0], 100)
temp1y = 0*temp1x+y[0]
line1, = line1x.plot(temp1x, temp1y)
point_an, = line1x.plot(temp1x[0], temp1y[0], 'ro')
text_P = plt.text(temp1x[0], temp1y[0], 'P', fontsize=16)

temp2x = np.linspace(p/2., x[0], 100)
k = (0 - y[0])/(p/2. - x[0])
b = -k*p/2.
temp2y = k*temp2x + b
line2, = line2x.plot(temp2x, temp2y,)

temp3x = x[0:1]
temp3y = y[0:1]
parabola, = parabolax.plot(temp3x, temp3y)
point_pa, = parabolax.plot(temp3x[0], temp3y[0], 'ro')
text_M = plt.text(temp3x[0], temp3y[0], 'M', fontsize=16)

pm = ((temp1x[0]-temp3x[0])**2 + (temp1y[0] - temp3y[0])**2)**0.5
fm = ((p/2. - temp3x[0])**2 + temp3y[0]**2)**0.5
text_distance = plt.text(4,0,"|PM|=%.3f, |FM|=%.3f"%(pm, fm), fontsize=16)


plt.grid('--')

def update(num):
    temp1x = np.linspace(-p/2., x[num], 100)
    temp1y = 0*temp1x+y[num]
    line1.set_xdata(temp1x)
    line1.set_ydata(temp1y)
    point_an.set_data(temp1x[0], temp1y[0])
    text_P.set_position((temp1x[0], temp1y[0]))

    temp2x = np.linspace(p/2., x[num], 100)
    k = (0 - y[num])/(p/2. - x[num])
    b = -k*p/2.
    temp2y = k*temp2x + b
    line2.set_xdata(temp2x)
    line2.set_ydata(temp2y)

    temp3x = x[0:num]
    temp3y = y[0:num]
    parabola.set_xdata(temp3x)
    parabola.set_ydata(temp3y)
    point_pa.set_data(x[num], y[num])
    text_M.set_position((x[num], y[num]))

    pm = ((temp1x[0] - x[num]) ** 2 + (temp1y[0] - y[num]) ** 2) ** 0.5
    fm = ((p / 2. - x[num]) ** 2 + y[num] ** 2) ** 0.5
    text_distance.set_text("|PM|=%.3f, |FM|=%.3f" % (pm, fm))

    return line1,



ani = animation.FuncAnimation(fig, update, np.arange(0, fp), interval=0, blit=True)
ani.save("parabola.mp4", fps=60)

plt.show()