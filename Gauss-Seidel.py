x = 0
y = 0 
z = 0

for i in range(10):
    x = (5-y-z)/3
    y = (2*x+z-20)/5
    z = (10-x-y)/7
  
    print("Iter=%d x = %0.2f y=%0.2f z = %0.2f"%(i+1,x,y,z))
