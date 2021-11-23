import matplotlib.pyplot as plt
import numpy as np
import math


MAX_VAL = 32
STEP = 1
HALF_MAX_VAL = MAX_VAL / 2
MAX_RADIUS = math.sqrt(HALF_MAX_VAL**2 + HALF_MAX_VAL**2)

# For non-center position
X_OFFSET = HALF_MAX_VAL
Y_OFFSET = HALF_MAX_VAL


def map(x, y):
    x_off = x-X_OFFSET
    y_off = y-Y_OFFSET
    radius = math.sqrt(x_off**2 + y_off**2)
    if radius == 0:
        return {'x': 0, 'y': 0}

    angle = 0
    if y_off == 0:
        angle = 0 if x > 0 else math.pi
    else:
        angle = math.atan(x_off / y_off)
    if (x_off < 0):
        angle += math.pi
    elif (x_off > 0 and y_off < 0):
        angle += 2 * math.pi
    angle_deg = math.degrees(angle)
    ret_x = radius / MAX_RADIUS * MAX_VAL
    ret_y = angle / (2 * math.pi) * MAX_VAL
    return {'x': ret_x, 'y': ret_y}


def unmap(x, y):
    angle = y / MAX_VAL * 2 * math.pi
    x_dir = math.cos(angle)
    y_dir = math.sin(angle)
    radius = x
    ret_x = X_OFFSET + x_dir * radius
    ret_y = Y_OFFSET + y_dir * radius
    return {'x': ret_x, 'y': ret_y}


x = np.tile(np.arange(0, MAX_VAL, STEP), MAX_VAL)
y = np.empty(0, dtype=int)
for i in range(0, MAX_VAL, STEP):
    y = np.concatenate((y, np.ones(MAX_VAL, dtype=int) * i))

colors = np.arange(0, 100, 100 / len(x))

plt.scatter(x, y, c=colors, cmap='rainbow')
plt.show()

for i in range(0, len(x)):
    mapped = map(x[i], y[i])
    x[i] = mapped['x']
    y[i] = mapped['y']



plt.scatter(x, y, c=colors, cmap='rainbow')
plt.show()
