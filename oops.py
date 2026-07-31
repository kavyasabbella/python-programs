# Program: Classes and Objects
# Description: This program demonstrates basic Object-Oriented Programming
# concepts in Python using a Student class.


# Create a Student class
class Student:

    # Constructor to initialize student details
    def __init__(self, name, course, college):
        self.name = name
        self.course = course
        self.college = college

    # Method to display student details
    def display_details(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Course:", self.course)
        print("College:", self.college)


# Take student details from the user
name = input("Enter student name: ").strip()
course = input("Enter course name: ").strip()
college = input("Enter college name: ").strip()

# Check whether all fields are filled
if not name or not course or not college:
    print("Invalid input! All fields are required.")

else:
    # Create an object of the Student class
    student = Student(name, course, college)

    # Call the method using the object
    student.display_details()
