'''
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
students = []  # This is a student list.



def register_student():
    print("Welcome to Aunt Esther Nursery School Registration")
    print("Please enter the following information:")

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    date_of_birth = input("Date of Birth : ")
    nursery_class = input("Nursery Class: ")
    location = input("Location: ")
    guardian_name = input("Guardian's Name: ")
    payment_status = input("Payment Status (yes or no): ")

    student = {
        'First Name': first_name,
        'Last Name': last_name,
        'Date of Birth': date_of_birth,
        'Class': nursery_class,
        'Location': location,
        'Guardian\'s Name': guardian_name,
        'Payment Status': payment_status,
    }

    students.append(student)
    print("Student registered successfully!") 

register_student()


def print_summary():
    print("Registered Students Summary")
    print(".............")

print_summary()




    
    
    


    
    
    
        
    
        
    
        
