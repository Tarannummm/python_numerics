#power iteration for eigen values
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float)
X=np.ones(3)
for i in range (10):
    Y=A@X
    m=np.max(np.abs(Y))
    Y=Y/m
    X=Y
    print(X,Y)

#monte carlo
import numpy as np 
f=lambda x:3*(x**2)-4
a=0
b=2
N=1000
u=np.random.uniform(0,1,N)
sum=0
for i in range(N):
    x=a+(b-a)*u[i]
    sum=sum+f(x)
avg=sum/N
I=(b-a)*avg
print(I)

#trapeziodal
import math 
f=lambda x:math.exp(x)
a=0
b=1
n=4 #any n
h=(b-a)/n
sum=f(a)+f(b)
for i in range(1-n):
    a=a+h
    sum=sum+2*f(a)
sum=sum+(h/2)
print(sum)

#simpsons 1/3
import math
f=lambda x:math.exp(x)
a=0
b=1
n=8 #n must be even
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

#simpsons 3/8
import math
f=lambda x:x**2-2
a=0
b=1
n=15
h=(b-a)/n
for i in range(1,n):
    a=a+h
    if i%3==0:
        sum=sum+2*f(a)
    else:
        sum=sum+3*f(a)
sum=sum*(3*h)/8
print("approximate integral: ",sum)