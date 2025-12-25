import numpy as np
A=np.array([[5,2,0],[2,1,0],[-3,4,2]],dtype=float)
X=np.ones(3)
for i in range(10):
    Y=A@X
    m=np.max(np.abs(Y))
    Y=Y/m
    X=Y
    print(m,Y) 