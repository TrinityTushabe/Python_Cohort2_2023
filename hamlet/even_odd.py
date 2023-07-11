num_range = int(input("Enter your Number: ")) # variable thats storing the number entered/range on the keyboard

print("Even Numbers in the Range are :") #printing to screen
for n in range(1, num_range+1):             # this is the range from 1 onwards
    if(n%2==0):                             # checking for the condition of a number being even
        print(n)                            #printing

print("Odd Numbers in the Range are")       
for n in range(1, num_range+1):
    if(n%2!=0):                            # checking for the condition of a number being odd
        print(n)
