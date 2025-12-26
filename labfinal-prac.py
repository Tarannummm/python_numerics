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