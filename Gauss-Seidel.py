x = 0
y = 0 
z = 0

for i in range(10):
    x = (5-y-z)/3
    y = (2*x+z-20)/5
    z = (10-x-y)/7
  
    print("Iter=%d x = %0.2f y=%0.2f z = %0.2f"%(i+1,x,y,z))



import matplotlib.pyplot as plt

#2x + y = 3, x - 3y = -5

x = 0
y = 0

solX=[]
solY = []
for i in range(6):
    x = (3-y)/2
    y = (x+5)/3
    solX.append(x)
    solY.append(y)

plt.plot(solX)
plt.plot(solY)

plt.xlabel('Iteration')
plt.ylabel('Solution')

plt.legend()
plt.show()

