'''
QUESTION 2.
 imagine there is a school called aunt esther nursery school looking for software program to register new nursery pupils in baby class.
 create an intractive program with atleast one function.
 names(both names)
 date of birth
 her class
 location where the pupil is coming from.
 guardian's name
 state of payment(yes or no)
 print the summary of the registered pupil.
 amoount of money every student should pay.(hard coded)
 the captured values should be appended in a list called students.
 the assignment should be pushed to git.
 even yesterdays work should be sent there.
'''

students = []  # List to store registered students

def register_student():
    print("***** Aunt Esther Nursery School - New Student Registration *****")
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    date_of_birth =str(input("Enter student's date of birth (DD/MM/YYYY): "))
                  
    class_name = input("Enter the class for the student: ")
    location = input("Enter the location the student is coming from: ")
    guardian_name =input("Enter the guardian's name: ")
    payment_status =input("Has the payment been made? (yes/no): ")

    # A dictionary to store student information.
    student = {
        "First Name": first_name,
        "Last Name": last_name,
        "Date of Birth": date_of_birth,
        "Class": class_name,
        "Location": location,
        "Guardian's Name": guardian_name,
        "Payment Status": payment_status
    }

    students.append(student)  #  To add the students to the list

    print("\n***** Summary of Registered Pupil *****")
    for key, value in student.items():
        print(key + ": " + value)

    print("Amount of money every student should pay: shs.250000")  # Amount of school fees to be paid.

# Register a new student(calling the function)
register_student()



