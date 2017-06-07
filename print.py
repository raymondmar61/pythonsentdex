#Sentdex
#Video 3 Python 3 Tutorial Print Function and Strings
#Video 4 Python 3 Programming Tutorial Math
#Video 5 Python 3 Programming Tutorial Variables
#Video 6 Python 3 programming tutorial While Loop
#Video 7 Python 3 Programming Tutorial - For loop
#Video 8 Python 3 Programming Tutorial If Statement
#Video 9 Python 3 Programming Tutorial If Else
#Video 10 Python 3 Programming Tutorial If Elif Else

#Video 3 Python 3 Tutorial Print Function and Strings
print("This is an example of print function.")
print("We're going to the store.")
print('We\'re going to the store.')
print("One string together using plus sign." + "Two string together using plus sign.  Plus sign needs spaces in strings.")
print("One string together using comma." , "Two string together using comma.  Comma no spaces in strings.")
print("Comma is good for numbers",5,"Obviously plus sign doesn't work because numbers intepret plus sign as addition.  Duh!")
print("Hi "+str(5))
print(int("8") + 5) #prints 13
print(float("8.5") + 5) #prints 13.5
print("\n")

#Video 4 Python 3 Programming Tutorial Math
print(4**4) #prints 256
print("\n")

#Video 5 Python 3 Programming Tutorial Variables
exampleVarCamelCase = 55 #camel casing exampleVar for which the V, C, and C are capitalized
print(exampleVarCamelCase)
x,y = (3,5) #unpacking
print(x)
print(y)
print("\n")

#Video 6 Python 3 programming tutorial While Loop
condition = 1
while condition < 10:
	print(condition)
	condition +=1
'''
while True:  #infinite loop
	print("doing stuff")
'''
print("\n")

#Video 7 Python 3 Programming Tutorial - For loop
exampleListUnpack = [1,5,6,1,6,7,8,9,345,53,5]
for eachNumber in exampleListUnpack:
	#print(eachNumber)
	print(eachNumber, end=" ")
	print("continue program", end=" ")
print("\n")
for x in range(1, 11):
	print(x)
print("\n")

#Video 8 Python 3 Programming Tutorial If Statement
x = 5
y = 8
z = 5
a = 3
if x < y:
	print("x is less than y")
if z < y > x:
	print("y is greater than z and greater than x")
if z < y > x > a:
	print("y is greater than z and greater than x")
if z <= x:
	print("z is less than or equal to x")
if z == x:
	print("z is equal to x")
if z != y:
	print("z is not equal to y")
print("\n")

#Video 9 Python 3 Programming Tutorial If Else
x = 5
y = 8
if x > y:
	print("x is greater than y")
else:
	print("x is less than y")
print("\n")

#Video 10 Python 3 Programming Tutorial If Elif Else
x = 5
y = 10
z = 22
if x > y:
	print("x is greater than y")
elif x < z:
	print("x is less than z")
elif 5 > 2: #true, too.  elif x<z is the first true.  If statement stopped.
	print("5 is greater than 2")
else:
	print("if and elif(s) never ran")