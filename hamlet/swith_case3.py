# switch case using dict


# function to recieve inputs
def getInput():
    num1 = int(input("Please Enter Number: "))
    num2 = int(input("Please Enter Number: "))
    return num1,num2
# add function 
def add():
    x, y = getInput()
    return x + y
# sub function
def sub():
    x, y = getInput()
    return x - y
# mul function
def mul():
    x, y = getInput()
    return x * y
# div function
def div():
    x, y = getInput()
    return x // y

#error handling function

def errorHandler():
    return "invalid Entry"

# prompt user
print('''
        1. Add
        2. Sub
        3. Mul
        4.Div
    '''    )
# prompt user
pickOne = int(input("Enter Number: "))
# moving through the dictionary, user selects 1 - 4.each key refrences a function
cal = {
    1: add,
    2: sub,
    3:mul,
    4:div,
}

output = cal.get(pickOne,errorHandler)()
print(output)