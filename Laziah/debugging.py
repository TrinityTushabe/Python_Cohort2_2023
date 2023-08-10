
def Esther (Name, Position, Age, Location, Gaurdian, Paymentstatus):
    Fees = 500000
    balance = Fees - Paymentstatus
    Age = 2023 - Age
    if Paymentstatus != Fees:
        print("********************************************************")
        print("Thank you for registering")
        print("Regestration Summary")
        print("Student Names: ",Name," ",)
        print("Student age: ",Age)
        print("position:p ",)
        print("Location: ",Location)
        print("Dear ", Gaurdian," your current tuition fees balance is ", balance)
        print("Thanks for registering")
        print("********************************************************")
    else:
        print("********************************************************")
        print("Thank you for registering")
        print("Regestration Summary")
        print("Student Names: ",Name)
        print("Student age: ",Age)
        print("Grade: ",Position)
        print("Location: ",Location)
        print("Dear Gaurdian, your current tuition fees balance is ", balance)
        print("Thanks for registering")
        print("********************************************************")  


print("Welcome to Antie Esther Nursery School Regestry.")
Name = input("Kindly input name: ")
Age = input("Kindly input student birth year: ")
Position = input("Kindly input student grade: ")
Location = input("Kindly input student home location: ")
Gaurdian = input("Kindly input student gaurdian names: ")
Paymentstatus =input("Kindly input amount of tuition paid: ")
Esther(Name, Position, Age, Location, Gaurdian, Paymentstatus)
myList = []
myList.append('Name')
myList.append('Age')
myList.append('Position')
myList.append('Location')
myList.append('Gaurdian')
myList.append('Paymentstatus')



def sum():
    num1,num2 = (5,6)
    num3 = num1+num2
    print (num3)

sum()