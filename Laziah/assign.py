'''
#This code demonstrates the usage of functions.

'''

#It performs tests on given inputs.
def tests(test1, test2):
	if test1 == test2:
	#Check if test1 is equal to test2
		return test1
	else:
		#If test1 is not equal to test2
		return test2
#It allows the function to pass the value
#  of value test2 back to the caller.
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
Request the user to enter the marks for test1 and test2.

'''

#Perform some operations related to the given cwork.
def courseWrk(cswork):
	
	testsMark = tests(test1,test2)
	#Call the "test" function with arguments "test1" and "test2"
	avgtestsCswork = (cswork + testsMark)/2
	#This code calculates  the average of two variables: "cwork" "testsMarks".
	fnltestsCswork = avgtestsCswork * (40/100)
	#This code calculates  the final test score for cWork based on average test score (" avgtestCwork").
	print('..............................')
	#print a divider consisting of a series of dots.
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
#It prints the final coursework marks.
cswork = int(input('Please enter your course work Marks: '))
#Prompts the user to enter their coursework marks.
courseWrk(cswork)