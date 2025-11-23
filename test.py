
# # Program to check if a year is a leap year

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")
# if op == '+': print(a + b)
# elif op == '-': print(a - b)
# elif op == '*': print(a * b)
# elif op == '/': print(a / b)
# else: print("Invalid operator")


# n = int(input("Enter number: "))
# fact = 1
# for i in range(1, n + 1):
# fact *= i
# print("Factorial =", fact)



# x = 10
# if x > 0:
#     if x % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")



# a = 5
# b = 10
# c = 7
# if a > b and a > c:
#     print("A is largest")
# elif b > c:
#     print("B is largest")
# else:
#     print("C is largest")

# cube = lambda x: x**3
# print(cube(3))

# import matplotlib.pyplot as plt   

# x=[1,2,3]
# plt.plot(x)
# plt.show()


# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)



# import matplotlib.pyplot as plt

# solX = []   # will store values of x
# solY = []   # will store values of y

# # Suppose we calculate x and y in a loop
# for i in range(10):
#     x = i        # some example value
#     y = i*i      # y = i² (example)
    
#     solX.append(x)
#     solY.append(y)

# # Plotting the results
# plt.plot(solX, label='X values')   # plot solX
# plt.plot(solY, label='Y values')   # plot solY

# plt.xlabel('Iteration')            # x-axis name
# plt.ylabel('Solution')             # y-axis name

# plt.legend()                       # show legend box
# plt.show()                         # show the final graph

# student = {
#     "name": "Tarannum",
#     "age": 20,
#     "dept": "CSE"
# }

# print(student["name"])


# a = [2, 3, 2, 5, 3, 7, 7]

# unique = []
# for i in a:
#     if i not in unique:
#         unique.append(i)

# print(unique)


# num = 29
# flag = True

# for i in range(2, num):
#     if num % i == 0:
#         flag = False
#         break

# if flag:
#     print("Prime")
# else:
#     print("Not Prime")


# nums = [5, 3, 8, 1, 2]

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] > nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]

# print(nums)


nums = [2, 5, 7, 10, 15, 20, 25]
target = 15

low = 0
high = len(nums) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        found = True
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print("Found?" , found)
