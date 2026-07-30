# Program: String Operations
# Description: This program demonstrates common operations performed on a string.

# Take text from the user
text = input("Enter some text: ").strip()

# Check whether the user entered any text
if not text:
    print("Invalid input! Please enter some text.")

else:
    # Display the original text
    print("\nOriginal Text:", text)

    # Display basic string operations
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Title Case:", text.title())

    # Find the length of the string
    print("Number of characters:", len(text))

    # Reverse the string
    print("Reversed Text:", text[::-1])

    # Count words in the string
    words = text.split()
    print("Number of words:", len(words))

    # Check whether the text is a palindrome
    cleaned_text = text.replace(" ", "").lower()

    if cleaned_text == cleaned_text[::-1]:
        print("The text is a Palindrome.")
    else:
        print("The text is not a Palindrome.")
