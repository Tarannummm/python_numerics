
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


# nums = [2, 5, 7, 10, 15, 20, 25]
# target = 15

# low = 0
# high = len(nums) - 1
# found = False

# while low <= high:
#     mid = (low + high) // 2

#     if nums[mid] == target:
#         found = True
#         break
#     elif nums[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1

# print("Found?" , found)


# n = 5

# for i in range(1, n+1):
#     # spaces
#     for s in range(n-i):
#         print(" ", end="")
    
#     # numbers
#     for j in range(1, i+1):
#         print(j, end=" ")

#     print()


# for num in range(2, 51):
#     prime = True
    
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num, end=" ")

#insertion sort
# arr = [9, 5, 1, 4, 3]

# for i in range(1, len(arr)):
#     key = arr[i]
#     j = i - 1
    
#     while j >= 0 and arr[j] > key:
#         arr[j + 1] = arr[j]
#         j -= 1

#     arr[j + 1] = key

# print(arr)

#quick sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr)//2]
#     left = [x for x in arr if x < pivot]
#     mid  = [x for x in arr if x == pivot]
#     right= [x for x in arr if x > pivot]

#     return quick_sort(left) + mid + quick_sort(right)

# print(quick_sort([6, 3, 8, 5, 2, 7, 4]))

#merge sort
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]

#         merge_sort(left)
#         merge_sort(right)

#         i = j = k = 0
        
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1
        
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1
        
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1

# arr = [9, 4, 7, 3, 1, 6]
# merge_sort(arr)
# print(arr)
#stack
# stack = []

# # push
# stack.append(10)
# stack.append(20)
# stack.append(30)

# # pop
# print(stack.pop())
# print(stack.pop())

# print("Final Stack:", stack)


#queue

# queue = []

# # enqueue
# queue.append(10)
# queue.append(20)
# queue.append(30)

# # dequeue
# print(queue.pop(0))
# print(queue.pop(0))

# print("Final Queue:", queue)


#largest word
# text = "Python is the best programming language"
# words = text.split()

# largest = words[0]

# for w in words:
#     if len(w) > len(largest):
#         largest = w

# print("Largest word:", largest)


# text = "Anika Tarannum"
# vowels = "aeiouAEIOU"
# result = ""

# for ch in text:
#     if ch not in vowels:
#         result += ch

# print(result)
#remove duplicate
# s = "banana"
# result = ""

# for ch in s:
#     if ch not in result:
#         result += ch

# print(result)

#recursion fibonacci
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(10))


#find the missing number
nums = [1,2,3,4,5,6,8,9,10]
n = 10

expected = n * (n+1) // 2
actual = sum(nums)

print("Missing number:", expected - actual)
