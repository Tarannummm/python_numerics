import math

f = lambda x: math.exp(-x)-x
df = lambda x: -math.exp(-x)-1

x0 = 0
i = 1

tol = 0.001


while i <= 100:
    x1 = x0-f(x0)/df(x0)
    err = abs(x1-x0)
    print(err)

    if err < tol:
        print(f"No of iteration {i}")
        break
    x0 = x1
    i = i+1