import math

f = lambda x: x**2 - 2
a = 1
b = 2

r = math.sqrt(2)
tol = 0.0001

i = 1
while i <= 100:
    c = (a+b)/2
    err = abs(r-c)

    print(f"iter {i}: app_root: {c:.8f} error: {err:.8f}")

    if err < tol:
        break
    if f(c) > 0:
        b = c
    else:
        a = c
    i = i + 1