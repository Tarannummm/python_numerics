# import math

# f=lambda x: math.exp(-x)-x
# a=0
# b=1
# iter=1

# while iter<=5:
#     c = (a*f(b) - b*f(a)) / (f(b)-f(a))
#     print(" Iter: %d  App_root: %0.5f"%(iter,c))
#     a=b
#     b=c
#     iter=iter+1





















import math 
f = lambda x:math.exp(-x)-x
a=0
b=1
iter=1
while iter<=5:
    c=(a*f(b)-b*f(a))/(f(b)-f(a))
    print("iter :%d app_root:%0.5f"%(iter,c))
    a=b
    b=c
    iter=iter+1



















