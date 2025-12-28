#trapezoidal
#e^x**2
import math
f= lambda x:math.exp(x**2)
a=0
b=1
n=6
h=(b-a)/n
sum=f(a)+f(b)
for i in range(1,n):
    a=a+h
    sum=sum+2*f(a)
sum=sum*(h/2)
print(sum)


#simpson's 1/3 
#f=x**2+1 
import math
f=lambda x:x**2+1
a=0
b=12
n=6
h=(b-a)/n
sum=f(a)+f(b)
for i in range(1,n):
    a=a+h
    if i%2==0:
        sum=sum+2*f(a)
    else:
        sum=sum+4*f(a)
sum=sum*(h/3)
print(sum)

#simpson's 3/8
f=lambda x:x**2+1
a=0
b=12
n=6
h=(b-a)/n
sum=f(a)+f(b)
for i in range(1,n):
    a=a+h
    if i%3==0:
        sum=sum+2*f(a)
    else:
        sum=sum+3*f(a)
sum=sum*3*(h/8)
print(sum)
 
#weddles
f=lambda x:x**2+1
a=0
b=12
n=6
h=(b-a)/n
sum=0
x0=0
#as here n=6 so no loop needed
x1=x0+h
x2=x1+h
x3=x2+h
x4=x3+h
x5=x4+h
x6=x5+h
sum=sum+ (3*h/10*(f(x0)+5*f(x1)+f(x2)+6*f(x3)+f(x4)+5*f(x5)+f(x6)))
x0=x6
print(sum)
#heuns
import math
f=lambda x,y:x+y
x0=0
y0=1
h=0.01
xn=0.1
n=int((xn-x0)/h)
for i in range(n):
    k1=f(x0,y0)
    k2=f(x0+h,y0+k1+h)
    y=y0+h/2*(k1+k2)
    y0=y
    x0=x0+h
    print("iter :%d x=%f y=%f"%(i+1,x0,y0))