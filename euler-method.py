import math
f=lambda x,y:x+y
x0=0
y0=1
h=0.01
xn=0.1
n=int((xn-x0)/h)
for i in range(n):
    y=y0+h*f(x0,y0)
    x0=x0+h
    y0=y
    print("iter %d x=%f y=%f"%(i,x0,y))