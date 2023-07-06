
def person(name,dob,grade,location,guardian_names,sop):
    hi = 'Dear student: '
    years = 'Year of Birth: '
    caretaker = 'Your Guardians Name is: '
    areacode = 'Your location is: '
    
    print(hi+name)
    print(years+dob)
    print('Your grade is: ',grade)
    print(areacode+location)
    print(caretaker+guardian_names)
    if sop == 'paid':
        sop = "Yes"
    else:
        sop = "No"  
    
    print('Paid =',sop)
    
    
amount = 5000
print('Your Welcome To Aunty Esthers Nursery school....')
print('FEES:',amount)  
name = raw_input('please input your Student Name here: ') 
dob = raw_input('please input your Date of Birth here: ')
guardian_names = raw_input('Please insert the Guardians Names here: ') 
grade = input('Please input the Grades here: ')
sop = raw_input('Please insert the State Of Payment: ')
location = raw_input('please insert your Location here: ')
student = [name,dob,guardian_names,grade,location,]
print(student)

person(name,dob,grade,location,guardian_names,sop)



#imagine running aunty esther nursery school and its looking for a software program that will help it register new nursery students in baby class
#create a program that will store new students in baby class.
#create an interactive program with atleast one function.
#capture both names, date of birth, class, location,guardian names,state of payment(either yes or No)
# summary of registered students
# amount of money the student should pay.
# captured values should be appended in a list called student
# push the assignment on a git repo named python group2 and add everyone to be a contributor
# 
# assignment; Define 2 functions that can out put even and odd numbers using while loop.
#in a range of 100 in tens.(10,20,30s).