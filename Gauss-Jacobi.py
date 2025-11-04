a = 0 #x
b = 0 #y
c = 0 #z

for i in range(20):
    x = (5-b-c)/3
    y = (2*a+c-20)/5
    z = (10-a-b)/7
    a = x
    b = y
    c = z
    print("Iter=%d x = %0.2f y=%0.2f z = %0.2f"%(i+1,x,y,z))