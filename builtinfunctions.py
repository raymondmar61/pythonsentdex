#sentdex
#Video 34 Python 3 Built-in Functions
#Built-in Functions are functions no importing.  Functions are in the standard library.  Instructor covers some of the basic built-in functions.

number1 = -5
number2 = 5
print(abs(number1)) #prints 5
if abs(number1) == number2:
	print("These are the same")

numberlist = [5,2,6,7,8,0]
print(max(numberlist)) #prints 8
print(min(numberlist)) #prints 0
x = 5.622
print(round(x)) #prints 6
import math
print(math.floor(x)) #prints 5
print(math.ceil(x)) #prints 6

integerme = "55"
print(integerme) #prints 55
print(int(integerme)) #prints 55 converts to integer
print(float(integerme)) #prints 55.0 coverts to floor
stringme = 77
print(str(stringme)) #prints 77 <--string.  Not number.