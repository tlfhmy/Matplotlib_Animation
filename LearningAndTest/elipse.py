import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def makelinedata(x1,y1,x2,y2):
    if x1-x2 != 0:
        k = (y1-y2)/(x1-x2)
        b = y1 - k*x1
        x = np.linspace(x1, x2, 1000)
        y = k*x+b
    else:
        k = (x1 - x2) / (y1 - y2)
        b = x1 - k * y1
        y = np.linspace(y1, y2, 1000)
        x = k * y + b
    return x,y

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

a = 4
b = 2
c = (a**2-b**2)**0.5

theta = np.linspace(0, 2*np.pi, 1200)
x = a*np.cos(theta)
y = b*np.sin(theta)

fig = plt.figure(dpi=300)
plt.xlim(-a-1, a+1)
plt.ylim(-b-1, b+1)

ax = fig.add_subplot(111)

ax.plot(-c, 0, 'ro')
text_F1 = ax.text(-12**0.5, 0, "F1", fontsize=16)
ax.plot(c, 0, 'ro')
text_F2 = ax.text(12**0.5, 0, "F2", fontsize=16)

M = (x[0], y[0])
M_point, = ax.plot(M[0], M[1], 'ro')
textM = ax.text(M[0], M[1], 'M', fontsize=16)

line_MF1 = makelinedata(M[0], M[1], -c, 0)
MF1_line, = ax.plot(line_MF1[0], line_MF1[1])

line_MF2 = makelinedata(M[0], M[1], c, 0)
MF2_line, = ax.plot(line_MF2[0], line_MF2[1])

elipse_M, =ax.plot(x[0:1],y[0:1])

text_sum = ax.text(-2.5, 2.5, "|MF1|+|MF2|=%.3f"%2*a, fontsize=16)

def update(num):
    M = (x[num], y[num])
    textM.set_position((M[0], M[1]))
    elipse_M.set_data(x[0:num], y[0:num])


    M_point.set_data(x[num], y[num])
    line_MF1 = makelinedata(M[0], M[1], -c, 0)
    MF1_line.set_data(line_MF1[0], line_MF1[1])
    line_MF2 = makelinedata(M[0], M[1], c, 0)
    MF2_line.set_data(line_MF2[0], line_MF2[1])

    dis = distance(M[0],M[1], -c, 0) + distance(M[0], M[1], c, 0)
    text_sum.set_text("|MF1|+|MF2|=%.3f" % dis)
    return MF1_line,

ani = animation.FuncAnimation(fig, update, np.arange(0,1200), blit=True)
ani.save("elipse.mp4", fps=60)