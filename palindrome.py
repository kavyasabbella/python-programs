# Program: Palindrome Checker
# Description: This program checks whether the entered text is a palindrome.

# Take text from the user
text = input("Enter a word or text: ").strip()

# Check if the user entered something
if not text:
    print("Invalid input! Please enter some text.")

else:
    # Convert the text to lowercase for case-insensitive comparison
    cleaned_text = text.lower()

    # Check whether the text is the same when reversed
    if cleaned_text == cleaned_text[::-1]:
        print(text, "is a Palindrome")
    else:
        print(text, "is not a Palindrome")
