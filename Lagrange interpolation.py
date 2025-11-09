fun=lambda x: 2**x
exact=fun(2.1)
print(f'exact ={exact}')
x = [0, 1, 2, 3]
y = [1, 2, 4, 8]
n = len(x)
xx = 2.1
f = 0
for i in range(n):
    L = 1
    for j in range(n):
        if i != j:
            L *= (xx - x[j]) / (x[i] - x[j])
    f= f+y[i] * L
print("Interpolated value at x =", xx, "is y =", f)
err=abs(exact-f)/exact*100
print(f'Error={err}%')