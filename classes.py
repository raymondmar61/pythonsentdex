#sentdex
#Video 21 Python 3 Programming Tutorial - Classes
#Video 22 Python 3 Frequently Asked Questions
#Video 23 Python 3 Getting user input
#Video 24 Python 3 Statistics (Mean, Standard Deviation)

class calculator:
	def addition(x,y):
		added = x + y
		print(added)
	def subtraction(x,y):
		subtract = x - y
		print(subtract)
	def multiplication(x,y):
		multiply = x * y
		print(multiply)
	def division(x,y):
		divide = x / y
		print(divide)

calculator.multiplication(3,5)  #returns 15
calculator.addition(5,2) #returns 7

# shebang line is #!usr/bin/python.  On Linux, it shows the path to Python.

#people can use the code as a module
def epic():
	print("wow this is great!")

if __name__ == "__main__": 
	print("such great module!!!!")

x = input("What is your name? ")
print("Hello", x)
print("Hello " + x)

import statistics
example_list = [4, 6, 2, 6, 7, 8, 2, 5, 6, 78, 4, 6, 7, 2, 2, 2]

meanx = statistics.mean(example_list)
print(meanx) #prints 9.1975
medianx = statistics.median(example_list)
print(medianx) #prints 535
modex = statistics.mode(example_list)
print(modex) #prints 2
print("mode() error message when there are two numbers appearing same equal times")
standarddeviationx = statistics.stdev(example_list)
print(standarddeviationx) #prints 18.468779963314667
variancex = statistics.variance(example_list)
print(variancex) #prints 341.09583333333336
