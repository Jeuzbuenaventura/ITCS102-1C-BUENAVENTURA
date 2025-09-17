
print("ODD NUMBER ACCUMULATOR")
print("Enter 10 numbers. We'll sum only the odd ones!\n")

odd_sum = 0
count = 1

while count <= 10:
    number = int(input(f"Enter number {count}: "))
    if number % 2 != 0:
        odd_sum += number
    count += 1

print("\n\t\tThe total sum of odd numbers is:", odd_sum)
