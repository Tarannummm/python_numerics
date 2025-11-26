# 3. a) Use the Gauss–Seidel method to solve the following system of linear equations:
# 10x + 2y + z = 9
# 2x + 10y + 3z = 19
# x + 3y + 10z = 0
# Start with the initial approximation of x =0, y=0, z = 0, perform 5 iteration
# b) Draw the graph as the code shows

# import math
# import matplotlib.pyplot as plt
# x=0
# y=0
# z=0
# solx=[]
# soly=[]
# solz=[]


# for i in range(5):
#     x=(9-2*y-z)/10
#     y=(19-2*x-3*z)/10
#     z=(-x-3*y)/10
#     solx.append(x)
#     soly.append(y)
#     solz.append(z)
#     print(x,y,z)
# plt.plot(solx,label='x')
# plt.plot(soly,label='y')
# plt.plot(solz,label='z')

# plt.grid()
# plt.legend()
# plt.show()

# **“Use the Jacobi method to solve the following system of equations for 5 iterations.

# Start with x = 0, y = 1, z = 0.”**

# And the equations must be:

# 10x + 2y + z = 9
# 2x + 10y + 3z = 19
# x + 3y + 10z = 0

import math
import matplotlib.pyplot as plt
a=0
b=1
c=0
solx=[]
soly=[]
solz=[]
for i in range(5):
    x=(9-2*b-c)/10
    y=(19-2*a-3*c)/10
    z=(-a-3*b)/10
    solx.append(x)
    soly.append(y)
    solz.append(z)
    a=x
    b=y
    c=z
    print(x,y,z)
plt.plot(solx,label='x')
plt.plot(soly,label='y')
plt.plot(solz,label='z')
plt.legend()
plt.grid()
plt.show()
