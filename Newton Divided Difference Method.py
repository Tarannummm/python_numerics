import math as m
x = [1, 2, 2,3]
y = [4, 5, 4,8]
n = len(x)
xx = 1.5

# Initialize divided difference table
F = []
for i in range(n):
    F.append([0]*n)  #F = [[0 for _ in range(n)] for _ in range(n)]
    F[i][0] = y[i]

# Compute divided differences
for j in range(1, n):
    for i in range(n - j):
        F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])

# Newton interpolation
p = F[0][0]
product = 1
for i in range(1, n):
    product *= (xx - x[i - 1])
    p += F[0][i] * product
func = lambda x : 2 ** x
trueValue = func(xx)
abs_err = abs(trueValue - p)

# multiply by (x - x[i-1])
# add current term to p
per_err = abs(((trueValue - p) / trueValue) * 100)
print(f"Interpolated value at x = {xx} is {p:0.6f}\nAbs.Error: {abs_err:.5f}\n%Error: {per_err:.5f}")