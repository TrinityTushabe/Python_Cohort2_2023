
student_infor = []

name = input("Enter the Students Name: ")
age = input("Enter the Students Date of birth: ")
parents_names = input("Enter Parents/Guadians Name: ")
grade = input("What Grade are they in upper class or lower class?: ")



def payment():
    receit_no = int(input("Please Enter receipt Number: "))
    paid = (123, 456, 789)
    for receit_no in paid:
        if receit_no == paid:
            print("Paid")
            break
    
    else:
        print("Outstang Payment")

        return

payment()

payment_check = payment

student_infor.append(name)

student_infor.append(age)

student_infor.append(parents_names)

student_infor.append(grade)

student_infor.append(payment_check)

print(student_infor)

    
    
