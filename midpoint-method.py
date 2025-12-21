import math
f=lambda x,y:x+y
x0=0
y0=1
h=0.01
xn=0.1
n=int((xn-x0)/h)
for i in range(n):
    k1=f(x0,y0)
    k2=f(x0+h,y0+k1*h/2)
    y=y0+h/2*(k1+k2)
    y0=y
    x0=x0+h
    print("iter :%d x=%f y=%f"%(i+1,x0,y0))