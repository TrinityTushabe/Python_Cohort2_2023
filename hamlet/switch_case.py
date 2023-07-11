# switch case using lists

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
# prompt user
print('''
        1. Add
        2. Sub
        3. Mul
        4.Div
    '''    )
# prompt user
pickOne = int(input("Pick Calculation: "))
# moving through the list
cal = [add, sub, mul, div]
# pushing the indecies up,so the user can pick starting from 1, curry function
output = cal[pickOne - 1]()

print(output)







