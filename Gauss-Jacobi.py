

# 3x+y+z=5
# −2x+5y−z=−20
# x+y+7z=10




import matplotlib.pyplot as plt
a = 0 #x
b = 0 #y
c = 0 #z
 
solx=[]
soly=[]
solz=[] 
for i in range(20):
    x = (5-b-c)/3
    y = (2*a+c-20)/5
    z = (10-a-b)/7
    solx.append(x)
    soly.append(y)
    solz.append(z)
    a = x
    b = y
    c = z

plt.plot(solx)
plt.plot(soly)
plt.plot(solz)
    
plt.show()
plt.xlabel('Iteration')
plt.ylabel('Solution')
plt.title('Jacobi Iteration Convergence')

plt.legend()
