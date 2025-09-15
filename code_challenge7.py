
import random

total = 0

print("Generated Numbers:")

for i in range(10):
    number = random.randint(1, 100)
    print(number, end=" ")

    if number % 2 == 0:
        total += number

print("\n\n\tThe sum of even numbers is:", total)