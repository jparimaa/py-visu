import matplotlib.pyplot as plt
import numpy as np

MAX_VAL = 32
STEP = 1

x = np.tile(np.arange(0, MAX_VAL, STEP), MAX_VAL)
y = np.empty(0, dtype=int)
for i in range(0, MAX_VAL, STEP):
    y = np.concatenate((y, np.ones(MAX_VAL, dtype=int) * i))

colors = np.arange(0, 100, 100 / len(x))

plt.scatter(x, y, c=colors, cmap='rainbow')
plt.show()
