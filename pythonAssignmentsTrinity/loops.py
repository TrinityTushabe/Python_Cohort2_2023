"""
A function that prints out even and odd numbers in range of 100 
Each output shows whether its an even number or odd number

"""

def print_numbers():
    num = 0
    while num <= 100:
        if num % 2 == 0:
            print(num, "Even") # prints an even number
        else:
            print(num, "Odd") # prints an odd number
        num += 1

print_numbers()


