'''


'''


def tests(test1, test2):
	#defining the variables in test which are test1 and test2
	if test1 == test2:
		#check if test1 is equal to test2
		return test1
	else:
		#return test1 or else
		return test2
#or else return test2 if test1 is not equal to test2
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''the function test with parameters test1,and test defines the variables with the If condition of stating that if test1 is equal to test2,
return test1 or else return test2 if test1 is not equal to tes1.
test1 and test2 are type cast by the integer data type.


'''#the defined function coursewrk has a variable cswork. variable testsmark is asigned to tests with parameters test1,test2. 
#averagetsCswork is assigned the value of cswork plus testsmark to the remainder 2. 
#the code is printing the fnltestscswork results which are got from the avgtestscswork mulitplied by (40/100)

def courseWrk(cswork):
	#define variable courseWrk as cswork
	testsMark = tests(test1,test2)
	#variable testsMark is asigned tests(test1,test2)
	avgtestsCswork = (cswork + testsMark)/2
	#calculates the average of two variables "cswork and testmark"
	fnltestsCswork = avgtestsCswork * (40/100)
	#calculates the final test score for cwork based on average test score.
	print('..............................')
	#print a divider consisting of a series of dots
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
#print final tests cswork
cswork = int(input('Please enter your course work Marks: '))
#variable cswork has been type cast as an integer 
courseWrk(cswork)