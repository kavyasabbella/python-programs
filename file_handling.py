# Program: File Handling
# Description: This program demonstrates how to write to and read from a text file.

# Take text from the user
text = input("Enter some text to save in the file: ").strip()

# Check whether the user entered any text
if not text:
    print("Invalid input! Please enter some text.")

else:
    try:
        # Open the file in write mode and save the text
        with open("sample.txt", "w") as file:
            file.write(text)

        print("Text saved successfully.")

        # Open the file in read mode
        with open("sample.txt", "r") as file:
            content = file.read()

        # Display the content stored in the file
        print("\nContent of the file:")
        print(content)

    except OSError:
        # Handle errors that may occur while working with the file
        print("An error occurred while accessing the file.")
