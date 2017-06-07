#Sentdex
#Video 11 Python 3 Programming Tutorial - Functions
#Video 12 Python 3 Programming Tutorial - Function Parameters
#Video 13 Python 3 Programming Tutorial - Function Parameter Defaults

#Video 11 Python 3 Programming Tutorial - Functions
def example():
	print("basic function")
	z = 3+9
	print(z) #prints 12
example()
print("\n")

#Video 12 Python 3 Programming Tutorial - Function Parameters
#def simple_addition(num1=5, num2=3):
def simple_addition(num1, num2):
	answer = num1 + num2
	print("num1 is", num1)
	print("num2 is", num2)
	print(answer)
simple_addition(5,3)
print("\n")

#Video 13 Python 3 Programming Tutorial - Function Parameter Defaults
def simple(num1, num2):
	pass
def simple(num1,num2=5):
	print(num1,num2)
simple(2) #returns 2 5
def basic_window(width,height,font="times new roman",backgroundcolor="white",scrollbar=True):
	print(width, height, font, backgroundcolor)
basic_window(500,350) #returns 500 350 times new roman white
basic_window(500,350,"arial") #returns 500 350 arial white
basic_window(500,350,backgroundcolor="black") #returns 500 350 times new roman black