import math
import matplotlib.pyplot as plt

g = lambda x: math.exp(-x)
x = [i for i in range(15)]
y = [g(p) for p in x]

plt.plot(x, y)
plt.show()