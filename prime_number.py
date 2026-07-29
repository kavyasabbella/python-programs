# Program: Prime Number Checker
# Description: This program checks whether the entered number is a prime number.

try:
    # Take an integer from the user
    num = int(input("Enter an integer: "))

    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        print(num, "is not a Prime Number")

    else:
        is_prime = True

        # Check for factors from 2 up to the square root of the number
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        # Display the result
        if is_prime:
            print(num, "is a Prime Number")
        else:
            print(num, "is not a Prime Number")

except ValueError:
    # Handle input that is not an integer
    print("Invalid input! Please enter a valid integer.")
