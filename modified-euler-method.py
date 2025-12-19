import math
f=lambda x,y:x+y
x0=0
y0=1
h=0.01
xn=0.1
n=int((xn-x0)/h)
for i in range(n):
    y1=y0+h*f(x0,y0)
    x1=y0+f(x0,y0)
    x0=x0+h
    y_m=y0+h/2*(f(x0,y0)+f(x1,y1))
    x0=x1
    y0=y1
    print("iter %d x=%f y=%f"%(i+1,x0,y0))