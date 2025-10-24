

name = input("Hi, what is your name? --> ")
total = 0
odd_numbers = []

print("\n+++++++++++++++++++++++++++++")
print("\nODD NUMBER SELECTOR — press 0 to stop the loop.")

while True:
    try:
        num = int(input("\nEnter a number --> "))

        if num == 0:
            print("Loop Terminated.")
            break
        elif num % 2 == 1:
            print("Odd number detected!")
            total += num
            odd_numbers.append(num)
        elif num % 2 == 0:
            print("Even number detected.")
        else:
            print("Invalid input. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

print(f"\nHi, {name}! The summation of all odd numbers is {total}.")
print(f"The odd numbers are: {odd_numbers}")
