from activity23_1 import *

print("WELCOME TO MY COMILER PROGRAM")
name= input("Hi Vistitor, what is your name --> ")

print(f"Hi {name}, Select from the options below ")
print("A - Greet Name \nB - Greet with Name, Age, Location \n C- Traingle \n E- Exit")

isCont = True

while isCont == True:
    choice = input("Select from A - E --> ").Lower()

    if choice == 'a':
       name = input("Please state your name ")
       GreetWithName(name)
       continue
    elif choice == 'b':
        number = eval(input("Input amy number --> "))
        print(f"Factorial of {number} is {Factorial(number)} ")
        continue
    elif choice == 'c':
        GetTriangle()
        continue
    elif choice == 'e':
        print("program terminated ... ")
        break
    else:
        print("invalid choice ")
        continue
