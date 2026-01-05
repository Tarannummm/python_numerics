f = lambda x, y: x + y
x0 = 0
y0 = 1
h = 0.05
xn = 0.1
n = int((xn - x0) / h)

for i in range(n):
    k1 = f(x0, y0)
    k2 = f(x0 + 3/4*h, y0 + 3/4*k1*h)

    y = y0 + (k1/3 + 2/3*k2)
    y0 = y
    x0 = x0+h
    print(f"Iter: {i+1} x={x0} y={y}")