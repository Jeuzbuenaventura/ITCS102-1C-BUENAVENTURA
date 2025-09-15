
number = eval(input("Enter a number --> "))
factorial = 1

for x in range(1, number + 1):
    factorial *= x

print("The factorial of", number, "is", factorial)
