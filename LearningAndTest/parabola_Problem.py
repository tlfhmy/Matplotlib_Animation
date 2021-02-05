import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def makelinedata(x1, y1, x2, y2):
    if x1 - x2 != 0:
        k = (y1 - y2) / (x1 - x2)
        b = y1 - k * x1
        x = np.linspace(x1, x2, 1000)
        y = k * x + b
    else:
        k = (x1 - x2) / (y1 - y2)
        b = x1 - k * y1
        y = np.linspace(y1, y2, 1000)
        x = k * y + b
    return x, y


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def calc_k(x1, y1, x2, y2):
    if x1-x2 == 0.:
        return "inf"
    else:
        return (y2-y1)/(x2-x1)

def calc_linejopo(k, x1, y1, x2):
    return (x2, k*(x2-x1)+y1)


p = 4

y = np.linspace(8, -8, 1200)
x = (1/(2*p)) * (y**2)

min_y, max_y = min(y), max(y)
min_x, max_x = min(x), max(x)

plt.xlim(-p/2-1, max_x*1.1)
plt.ylim(min_y*1.1, max_y*1.1)


fig = plt.figure(dpi=300)
ax = fig.add_subplot(111)
ax.set(aspect=1)
ax.plot(x,y)
plt.grid()

aligment_data = makelinedata(-p/2, min_y, -p/2, max_y)
aligment_line, = ax.plot(aligment_data[0], aligment_data[1])

ax.plot(p/2, 0, 'ro')

F = (p/2, 0)
text_F = ax.text(p/2, 0, "F", fontsize=14)

A = (x[1], y[1])
text_A = ax.text(A[0], A[1], "A", fontsize=14)
point_A, = ax.plot(A[0], A[1], 'ro')

A1 = (-p/2, A[1])
text_A1 = ax.text(A1[0], A1[1], "A1", fontsize=14)
point_A1, = ax.plot(A1[0], A1[1], 'ro')


line_AA1_data = makelinedata(A1[0], A1[1], A[0], A[1])
line_AA1, = ax.plot(line_AA1_data[0], line_AA1_data[1])

line_AF_data = makelinedata(A[0], A[1], F[0], F[1])
line_AF, = ax.plot(line_AF_data[0], line_AF_data[1])

line_A1F_data = makelinedata(A1[0], A1[1], F[0], F[1])
line_A1F, = ax.plot(line_A1F_data[0], line_A1F_data[1])

B = (p**3/(2*(A[1]**2)), -(p**2)/(A[1]))
text_B = ax.text(B[0], B[1], "B", fontsize=14)
point_B, = ax.plot(B[0], B[1], "ro")

line_BF_data = makelinedata(B[0], B[1], F[0], F[1])
line_BF, = ax.plot(line_BF_data[0], line_BF_data[1])

B1 = (-p/2, B[1])
text_B1 = ax.text(B1[0], B1[1], "B1", fontsize=14)
point_B1, = ax.plot(B[0], B[1], "ro")

line_BB1_data = makelinedata(B[0], B[1], B1[0], B1[1])
line_BB1, = ax.plot(line_BB1_data[0], line_BB1_data[1])

line_B1F_data = makelinedata(B1[0], B1[1], F[0], F[1])
line_B1F, = ax.plot(line_B1F_data[0], line_B1F_data[1])

P = (8, 8)
text_P = ax.text(P[0], P[1], "P", fontsize=14)
point_P = ax.plot(P[0], P[1], "ro")

km = calc_k(P[0], P[1], A[0], A[1])
if km != "inf":
    M = calc_linejopo(km, A[0], A[1], -p/2)
    text_M = ax.text(M[0], M[1], "M", fontsize=14)
    point_M, = ax.plot(M[0], M[1])

    line_MF_data = makelinedata(M[0], M[1], F[0], F[1])
    line_MF, = ax.plot(line_MF_data[0], line_MF_data[1])

    line_PM_data = makelinedata(M[0], M[1], P[0], P[1])
    line_PM, = ax.plot(line_PM_data[0], line_PM_data[1])

    kn = calc_k(B[0], B[1], P[0], P[1])
    N = calc_linejopo(kn, B[0], B[1], -p/2)
    text_N = ax.text(N[0], N[1], "N", fontsize=14)

    line_NF_data = makelinedata(N[0], N[1], F[0], F[1])
    line_NF, = ax.plot(line_NF_data[0], line_NF_data[1])

    line_PN_data = makelinedata(P[0], P[1], N[0], N[1])
    line_PN, = ax.plot(line_PN_data[0], line_PN_data[1])

    txt1 = ax.text(10.0, 1, "A1F*B1F = %.3f"%((A1[0]-F[0])*(B1[0]-F[0])+(A1[1]-F[1])*(B1[1]-F[1])), fontsize=14)
    txt2 = ax.text(10.0, -1, "MF*NF = %.3f"%((M[0]-F[0])*(N[0]-F[0])+(M[1]-F[1])*(N[1]-F[1])), fontsize=14)

def update(num):
    A = (x[num], y[num])
    text_A.set_position((A[0], A[1]))
    point_A.set_data(A[0], A[1])

    A1 = (-p / 2, A[1])
    text_A1.set_position((A1[0], A1[1]))
    point_A1.set_data(A1[0], A1[1])

    line_AA1_data = makelinedata(A1[0], A1[1], A[0], A[1])
    line_AA1.set_data(line_AA1_data[0], line_AA1_data[1])

    line_AF_data = makelinedata(A[0], A[1], F[0], F[1])
    line_AF.set_data(line_AF_data[0], line_AF_data[1])

    line_A1F_data = makelinedata(A1[0], A1[1], F[0], F[1])
    line_A1F.set_data(line_A1F_data[0], line_A1F_data[1])

    B = (p ** 3 / (2 * (A[1] ** 2)), -(p ** 2) / (A[1]))
    text_B.set_position((B[0], B[1]))
    point_B.set_data(B[0], B[1])

    line_BF_data = makelinedata(B[0], B[1], F[0], F[1])
    line_BF.set_data(line_BF_data[0], line_BF_data[1])

    B1 = (-p / 2, B[1])
    text_B1.set_position((B1[0], B1[1]))
    point_B1.set_data(B[0], B[1])

    line_BB1_data = makelinedata(B[0], B[1], B1[0], B1[1])
    line_BB1.set_data(line_BB1_data[0], line_BB1_data[1])

    line_B1F_data = makelinedata(B1[0], B1[1], F[0], F[1])
    line_B1F.set_data(line_B1F_data[0], line_B1F_data[1])


    km = calc_k(P[0], P[1], A[0], A[1])
    if km != "inf":
        M = calc_linejopo(km, A[0], A[1], -p / 2)
        text_M.set_position((M[0], M[1]))
        point_M.set_data(M[0], M[1])

        line_MF_data = makelinedata(M[0], M[1], F[0], F[1])
        line_MF.set_data(line_MF_data[0], line_MF_data[1])

        line_PM_data = makelinedata(M[0], M[1], P[0], P[1])
        line_PM.set_data(line_PM_data[0], line_PM_data[1])

        kn = calc_k(B[0], B[1], P[0], P[1])
        N = calc_linejopo(kn, B[0], B[1], -p / 2)
        text_N.set_position((N[0], N[1]))

        line_NF_data = makelinedata(N[0], N[1], F[0], F[1])
        line_NF.set_data(line_NF_data[0], line_NF_data[1])

        line_PN_data = makelinedata(P[0], P[1], N[0], N[1])
        line_PN.set_data(line_PN_data[0], line_PN_data[1])

        txt1.set_text("A1F*B1F = %.3f" % ((A1[0] - F[0]) * (B1[0] - F[0]) + (A1[1] - F[1]) * (B1[1] - F[1])))
        txt2.set_text("MF*NF = %.3f" % ((M[0] - F[0]) * (N[0] - F[0]) + (M[1] - F[1]) * (N[1] - F[1])))

    return line_AA1,

ani = animation.FuncAnimation(fig, update, np.arange(0,1200), blit=True)
ani.save("paraproblem.mp4", fps=60)

# plt.plot(x,y)
# plt.show()