
def reG(firstName, lastName, birthYear, graDe, LocAtion, Gaurdian, StateOfpay):
    Fees = 500000
    balance = Fees - StateOfpay
    Age = 2023 - birthYear
    if StateOfpay != Fees:
        print("********************************************************")
        print("Thank you for registering")
        print("Regestration Summary")
        print("Student Names: ",firstName," ",lastName)
        print("Student age: ",Age)
        print("Grade: ",graDe)
        print("Location: ",LocAtion)
        print("Dear ", Gaurdian," your current tuition fees balance is ", balance)
        print("Thanks for registering")
        print("********************************************************")
    else:
        print("********************************************************")
        print("Thank you for registering")
        print("Regestration Summary")
        print("Student Names: ",firstName," ",lastName)
        print("Student age: ",Age)
        print("Grade: ",graDe)
        print("Location: ",LocAtion)
        print("Dear Gaurdian, your current tuition fees balance is ", balance)
        print("Thanks for registering")
        print("********************************************************")  


print("Welcome to Antie Esther Nursery School Regestry.")
firstName = raw_input("Kindly input student first name: ")
lastName = raw_input("Kindly input student last name: ")
birthYear = input("Kindly input student birth year: ")
graDe = input("Kindly input student grade: ")
LocAtion = raw_input("Kindly input student home location: ")
Gaurdian = raw_input("Kindly input student gaurdian names: ")
StateOfpay = input("Kindly input amount of tuition paid: ")
reG(firstName, lastName, birthYear, graDe, LocAtion, Gaurdian, StateOfpay)

myList = []
myList.append(firstName)
myList.append(lastName)
myList.append(birthYear)
myList.append(graDe)
myList.append(LocAtion)
myList.append(Gaurdian)
myList.append(StateOfpay)
