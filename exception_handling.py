# Program: Exception Handling
# Description: This program demonstrates how Python handles common errors
# using try, except, else, and finally.

try:
    # Take two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Divide the first number by the second number
    result = num1 / num2

except ValueError:
    # Handle non-numeric input
    print("Invalid input! Please enter valid numbers.")

except ZeroDivisionError:
    # Handle division by zero
    print("Error! A number cannot be divided by zero.")

else:
    # This block runs when no exception occurs
    print("Result:", result)

finally:
    # This block always runs
    print("Program execution completed.")
