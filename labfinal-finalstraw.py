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
n=15 #must be multiple of 3
h=(b-a)/n
for i in range(1,n):
    a=a+h
    if i%3==0:
        sum=sum+2*f(a)
    else:
        sum=sum+3*f(a)
sum=sum*(3*h)/8
print("approximate integral: ",sum)

#weddles
import math 
x=lambda x:math.exp(x)
a=0
b=1
n=12
h=(b-a)/n
x0=0
sum=0
for i in range(2):
    x1=x0+h
    x2=x1+h
    x3=x2+h
    x4=x3+h
    x5=x4+h
    x6=x5+h
    sum=sum+(3*h/10*(f(x0)+5*f(x1)+f(x2)+6*f(x3)+f(x4)+5*f(x5)+f(x6)))
    x0=x6
print(sum)

#euler
import math
f=lambda x,y:x+y
x0=0
y0=1
h=0.01
xn=0.1
n=int((xn-x0)/h)
for i in range(n):
    y=y0+h*f(x0,y0)
    y0=y
    x0=x0+h
print(i,x0,y)

#modified euler
f=lambda x,y:x+y
x0=0
y0=1
h=0.01
xn=0.1
n=int((xn-x0)/h)
for i in range(n):
    y1=y0+h*f(x0,y0)
    x1=x0+h
    y_m=y+(h/2)*f(x0,y0)+f(x1,y1)
    y0=y_m
    x0=x1
    print(i+1,x0,y0)
#modified euler
import math

f = lambda x, y: x + y

x0 = 0
y0 = 1
h = 0.01
xn = 0.1

n = int((xn - x0) / h)

for i in range(n):
    y1 = y0 + h * f(x0, y0)          # predictor
    x1 = x0 + h

    y = y0 + h/2 * (f(x0, y0) + f(x1, y1))  # corrector

    x0 = x1
    y0 = y

    print("iter %d x=%f y=%f" % (i+1, x0, y0))


#heuns
import math
f=lambda x,y:x+y
x0=0
y0=1 #y(0)=1
h=0.01
xn=5 #y(5)=?
n=int((xn-x0)/h)
for i in range(n):
    k1=f(x0,y0)
    k2=f(x0+h,y0+h*k1)
    y=y0+h/2*(k1+k2)
    y0=y
    x0=x0+h
    print(i+1,x0,y0)
#midpoint
import math

f = lambda x, y: y * (1 - x)

x0 = 0
y0 = 1
h = 0.1
xn = 5

n = int((xn - x0) / h)

for i in range(n):
    k1 = f(x0, y0)
    k2 = f(x0 + h/2, y0 + k1*h/2)
    y = y0 + h * k2        # Midpoint Method
    y0 = y
    x0 = x0 + h

    print("iter :%d x=%f y=%f" % (i+1, x0, y0))
#midpoint
import math
f=lambda x,y:x+y
x0=0
y0=1
h=0.01
xn=5
n=int((xn-x0)/h)
for i in range(n):
    k1=f(x0,y0)
    k2=f(x0+h/2,y0+k1*h/2)
    y=y0+h*k2
    y0=y
    x0=x0+h
    print(i+1,x0,y0)

#ralstons
import math
f=lambda x,y:x+y
x0=0
y0=1
h=0.01
xn=5
n=int((xn-x0)/h)
for i in range(n):
    k1=f(x0,y0)
    k2=f(x0+3/4*h,y0+3/4*h*k1)
    y=y0+(k1/3+2/3*k2)
    y0=y
    x0=x0+h
    print(i+1,x0,y0)

#finite difference 
import numpy as np

# Number of subintervals
n = 4                     # you can change this
h = 1.0 / n               # step size

# Grid points
x = np.linspace(0, 1, n+1)

# Number of unknowns (interior points)
N = n - 1

# Coefficient matrix A
A = np.zeros((N, N))
for i in range(N):
    A[i, i] = -2
    if i > 0:
        A[i, i-1] = 1
    if i < N-1:
        A[i, i+1] = 1

# Right-hand side vector
b = -2 * h**2 * np.ones(N)

# Solve linear system
y_inner = np.linalg.solve(A, b)

print(y_inner)