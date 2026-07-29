# Program: Fibonacci Series
# Description: This program generates the Fibonacci series for a given number of terms.

try:
    # Take the number of terms from the user
    n = int(input("Enter the number of terms: "))

    # Check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer.")

    else:
        first = 0
        second = 1

        print("Fibonacci Series:")

        # Generate and display the Fibonacci series
        for i in range(n):
            print(first, end=" ")

            next_number = first + second
            first = second
            second = next_number

except ValueError:
    # Handle input that is not an integer
    print("Invalid input! Please enter a valid integer.")
