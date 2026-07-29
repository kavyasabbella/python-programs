# Program: Armstrong Number Checker
# Description: This program checks whether the entered number is an Armstrong number.

try:
    # Take an integer from the user
    num = int(input("Enter a non-negative integer: "))

    # Armstrong numbers are checked for non-negative integers
    if num < 0:
        print("Please enter a non-negative integer.")

    else:
        # Find the number of digits
        digits = len(str(num))

        # Calculate the sum of each digit raised to the power of total digits
        total = sum(int(digit) ** digits for digit in str(num))

        # Check whether the calculated sum is equal to the original number
        if total == num:
            print(num, "is an Armstrong Number")
        else:
            print(num, "is not an Armstrong Number")

except ValueError:
    # Handle input that is not an integer
    print("Invalid input! Please enter a valid integer.")
