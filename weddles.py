import math
f = lambda x: math.exp(x)
a = 0
b = 1
n = 12         
h = (b - a) / n

sum = 0

x0 = 0         

for i in range(2): #as here n=12 so the loop will run 2 times 
    x1 = x0 + h
    x2 = x1 + h
    x3 = x2 + h
    x4 = x3 + h
    x5 = x4 + h
    x6 = x5 + h

    sum = sum + (3*h/10 * (f(x0)+5*f(x1) + f(x2) + 6*f(x3)+f(x4)+5*f(x5)+f(x6)))

    x0 = x6      

print(sum)
