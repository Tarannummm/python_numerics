import numpy as np

f=lambda x: 3*(x**2)+1
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