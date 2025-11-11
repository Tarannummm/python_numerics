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