import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

matplotlib.use("TkAgg")

fig, ax = plt.subplots()    # initiating plot, ax is area of graph, fig is surrounding borders

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

fig.patch.set_facecolor("black")
ax.set_facecolor("black")


x = [1, 40, 60]     # index aligns with the point -> p1 = (x[0], y[0])
y = [2, 35, 75]

vx = [0.4, 0.2, -0.1]
vy = [0.4, 0.1, -0.2]

colors = ["red", "green", "blue"]

p = ax.scatter(x, y, s=50, c=colors)

def motion(frame):
    global x, y

    for i in range(3):
        x[i] += vx[i]
        y[i] += vy[i]

    p.set_offsets(list(zip(x, y)))   # changing the format to [[x1, y1], [x2, y2], [x3, y3]]

    return p,

time.sleep(1) # short delay before animation starts so user can see

ani = FuncAnimation(fig, motion, frames=200, interval=20, blit=True, repeat=False)

plt.show()