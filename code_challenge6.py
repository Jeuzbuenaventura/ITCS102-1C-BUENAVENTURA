
number = eval(input("Enter a number: "))
factorial = 1

for i in range(number, 0, -1):
    factorial *= i
print("The factorial of",number, "is", factorial)
