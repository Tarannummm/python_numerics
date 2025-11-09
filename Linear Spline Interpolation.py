x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

n = len(x)
xx = 2.5

for i in range(n - 1):
    if (xx >= x[i]) and (xx <= x[i + 1]):
        S = y[i] + (y[i + 1] - y[i]) * (xx - x[i]) / (x[i + 1] - x[i])
        print("Interpolated value:", S)