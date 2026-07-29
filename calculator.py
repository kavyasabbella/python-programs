# Program: Simple Calculator
# Description: This program performs basic arithmetic operations on two numbers.

try:
    # Take two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display available operations
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Take the user's choice
    choice = input("Enter your choice (1/2/3/4): ")

    # Perform the selected operation
    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        # Prevent division by zero
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")

except ValueError:
    # Handle non-numeric input
    print("Invalid input! Please enter valid numbers.")
