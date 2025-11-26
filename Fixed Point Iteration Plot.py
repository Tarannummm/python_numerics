import math
import matplotlib.pyplot as plt

root = []
g = lambda x: math.exp(-x)
x0 = 0

for i in range(15):
    x1 = g(x0)
    root.append(x1)
    x0 = x1

plt.plot(root)
plt.show()


#fixed point
import math
import matplotlib.pyplot as plt

root = []
errors = []
g = lambda x: math.exp(-x)
x0 = 0

for i in range(15):
    x1 = g(x0)
    root.append(x1)
    error = abs(x1 - x0)
    errors.append(error)
    x0 = x1

plt.plot(root, label='Root')
plt.plot(errors, label='Error')
plt.legend()
plt.show()