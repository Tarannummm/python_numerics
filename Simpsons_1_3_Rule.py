import math
f=lambda x:math.exp(x)
a=0
b=1
n=10
h=(b-a)/n
sum=f(a)+f(b)
for i in range (1,n):
    a=a+h
    if i%2==0:
        sum=sum +2*f(a)
    else:
        sum= sum +4 *f(a)
sum=sum*(h/3)
print(sum)
