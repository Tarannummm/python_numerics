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