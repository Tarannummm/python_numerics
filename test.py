
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


n = int(input("Enter number: "))
fact = 1
for i in range(1, n + 1):
fact *= i
print("Factorial =", fact)