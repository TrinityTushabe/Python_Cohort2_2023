
def paye(salary,name,age,location,type_of_work):
   print("welcome sir!")
   rate = 0.3
   if salary >= 300000:  
      tax =rate*salary
      net_pay =salary-tax
      print("+++++++++++++++++++")
      print("Dear: ",name) 
      print("The tax payable is: ",tax)
      print("The  take salary is: ",net_pay)
      print()
      print ("............")
      print("Enjoy our services!")
   else:
      print("Dear",name)
      print("your salary is non taxable")
   
   print(age,name,location,type_of_work,salary)
    
print("you are welcome")
salary = input("please enter your salary here: ")
print(type(salary))

print("Well be back")
name =raw_input("please input your name here: ")
age =input("please enter your age: ")
location = raw_input("please enter your location here: ")
type_of_work = raw_input("please enter your type_of_work here: ")
paye(salary,name,location,type_of_work,age)





