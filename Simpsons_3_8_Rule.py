import math 
f=lambda x:x**2+1
a=0
b=1
n=12
h=(b-a)/n
sum=f(a)+f(b)
for i in range (1,n):
    a=a+h
    if i%3==0:
        sum=sum+2*f(a)
    else:
        sum=sum+3*f(a)
sum=sum*3*(h/8)
print("Approximate of integral =",sum)