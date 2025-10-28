import math

f=lambda x: math.exp(-x)-x
df=lambda x: -math.exp(-x)-1
x0=0
iter=1

while iter<=10:
    x1=x0-f(x0)/df(x0)
    err=abs(x1-x0)
    print(" Iter: %d  App_root: %0.5f Abs_err:%f"%(iter,x1,err))
    x0=x1
    iter=iter+1