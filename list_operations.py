# Program: List Operations
# Description: This program demonstrates basic operations on a Python list.

try:
    # Ask the user how many numbers they want to enter
    n = int(input("How many numbers do you want to enter? "))

    # Check if the entered number is positive
    if n <= 0:
        print("Please enter a positive integer.")

    else:
        numbers = []

        # Take numbers from the user and add them to the list
        for i in range(n):
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)

        # Display the original list
        print("\nOriginal List:", numbers)

        # Display basic list information
        print("Number of elements:", len(numbers))
        print("Largest number:", max(numbers))
        print("Smallest number:", min(numbers))
        print("Sum of numbers:", sum(numbers))

        # Sort the list
        numbers.sort()
        print("Sorted List:", numbers)

        # Reverse the list
        numbers.reverse()
        print("Reversed List:", numbers)

except ValueError:
    # Handle invalid input
    print("Invalid input! Please enter valid numbers.")
