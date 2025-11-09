import math as m

fun = lambda p: 2**p

x = [0,1,2,3]
y = [1,2,4,8]
n = len(x)
xx = 1.5
exact = fun(xx)
f = 0
for i in range(n):
    L = 1
    for j in range(n):
        if(i!=j):
            L *= ((xx-x[j])/(x[i]-x[j]))
    f += (L*y[i])
print("Value is: ",f)
print(f'Exact value is: {exact}')

err = abs(exact-f)/exact * 100

print(f'Error = {err} %')