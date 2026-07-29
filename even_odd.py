# Program: Even or Odd Number
# Description: This program checks whether the entered integer is even or odd.

try:
    # Take an integer from the user
    num = int(input("Enter an integer: "))

    # Check whether the number is divisible by 2
    if num % 2 == 0:
        print(num, "is an Even Number")
    else:
        print(num, "is an Odd Number")

except ValueError:
    # Handle input that is not an integer
    print("Invalid input! Please enter a valid integer.")
