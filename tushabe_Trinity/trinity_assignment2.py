'''
The constructor method in Python is a special method that is automatically called when an object of a class is created
It is defined within a class and takes the self parameter as its first argument, followed by any other parameters that need to be passed during object creation.
'''
class Student:
    def __init__(self, first_name, last_name, date_of_birth, class_name, location, guardian_name, payment_status): # Constructor method that initializes the student object with the provided attributes
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.class_name = class_name
        self.location = location
        self.guardian_name = guardian_name
        self.payment_status = payment_status

    def display_summary(self):
        print("----------------------------------------------------------------")
        # Display the summary of the registered pupils information
        print("\n+++++ Summary of Registered Pupil +++++")
        print("****************************************************************")
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Date of Birth:", self.date_of_birth)
        print("Class:", self.class_name)
        print("Location:", self.location)
        print("Guardian's Name:", self.guardian_name)
        print("Payment Status:", self.payment_status)
        print("Amount of money every student should pay: shs.900000")
        print("----------------------------------------------------------------")

    def print_payment_details(self):
        if self.payment_status == "yes":
            #Display the payment details for a student who has paid
            print("----------------------------------------------------------------")
            print("\n ++++++++++ Payment Details ++++++++++ ")
            print("Student Name:", self.first_name, self.last_name)
            print("Payment Status: Paid")
            print("Amount Paid: shs.900000")
            print("----------------------------------------------------------------")
        else:
            print("----------------------------------------------------------------")
            # Display the payment details for a student who has not paid
            print("\n ++++++++++ Payment Details ++++++++++ ")
            print("----------------------------------------------------------------")
            print("Student Name:", self.first_name, self.last_name) # Print the student's first name and last name
            print("Payment Status: Not Paid")
            print("Amount Due: shs.900000")
            print("----------------------------------------------------------------")

def register_student(students):
    print("----------------------------------------------------------------")
    print("++++ Little Tots Nursery School - New Student Registration ++++")
    print("----------------------------------------------------------------")
    # Prompt the user to enter student details
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    date_of_birth = input("Enter student's date of birth (DD/MM/YYYY): ")
    class_name = input("Enter the class for the student: ")
    location = input("Enter the location the student will be coming from: ")
    guardian_name = input("Enter the Parent/guardian's name: ")
    payment_status = input("Has the payment been made? (yes/no): ").lower() # Prompt user for payment status and convert input to lowercase


    while payment_status not in ["yes", "no"]:
        # Validate the payment status input
        print("Invalid payment status. Please enter 'yes' or 'no'.")
        payment_status = input("Has the payment been made? (yes/no): ").lower() # Prompt user for payment status and convert input to lowercase


     # Create a new student object with the provided details
    student = Student(first_name, last_name, date_of_birth, class_name, location, guardian_name, payment_status)
    students.append(student)  # Append the student to the list of students
    student.display_summary()
    student.print_payment_details()

# Create an empty list to store registered students
students = []

# Register a new student (calling the function)
register_student(students)

# Access the registered students in the list
for student in students:
    print("Student Name:", student.first_name, student.last_name)
    # Perform any additional operations with the registered students
