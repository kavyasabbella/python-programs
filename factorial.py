# Program: Factorial of a Number
# Description: This program calculates the factorial of a non-negative integer.

try:
    # Take a number from the user
    num = int(input("Enter a non-negative integer: "))

    # Check if the number is negative
    if num < 0:
        print("Factorial is not defined for negative numbers.")

    else:
        factorial = 1

        # Multiply numbers from 1 to the entered number
        for i in range(1, num + 1):
            factorial *= i

        # Display the result
        print("Factorial of", num, "is", factorial)

except ValueError:
    # Handle input that is not an integer
    print("Invalid input! Please enter a valid integer.")
