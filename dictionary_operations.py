# Program: Dictionary Operations
# Description: This program demonstrates basic operations on a Python dictionary.

# Create an empty dictionary
student = {}

# Take student details from the user
name = input("Enter student name: ").strip()
course = input("Enter course name: ").strip()
college = input("Enter college name: ").strip()

# Check whether all fields contain values
if not name or not course or not college:
    print("Invalid input! All fields are required.")

else:
    # Add the details to the dictionary
    student["Name"] = name
    student["Course"] = course
    student["College"] = college

    # Display the complete dictionary
    print("\nStudent Details:", student)

    # Display individual values
    print("Name:", student["Name"])
    print("Course:", student["Course"])
    print("College:", student["College"])

    # Display all keys
    print("Keys:", list(student.keys()))

    # Display all values
    print("Values:", list(student.values()))

    # Update a value in the dictionary
    new_course = input("\nEnter updated course name or press Enter to skip: ").strip()

    if new_course:
        student["Course"] = new_course
        print("Updated Student Details:", student)
    else:
        print("No changes made.")
