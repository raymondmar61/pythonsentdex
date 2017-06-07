#Sentdex 3 Print Function and Strings, 4 Math, 5 Variables, 6 While Loop, 7 For loop, 8 If Statement, 9 If Else, 10 If Elif Else, 11 Functions, 12 Function Parameters, 13 Function Parameter Defaults, 14 Global and Local Variables, 18 Writing to file, 19 Appending Files, 20 Read from a file, 21 Classes, 22 Frequently asked questions, 23 Getting user input, 24 Statistics (Mean, Standard Deviation), 25 Module Import Syntax, 26 Making Modules, 27 Lists and Tuples, 28 List Manipulation, 29 Multi-dimensional List, 30 Reading from a CSV spreadsheet, 31 Try and Except error Handling, 32 Multi-line Print, 33 Dictionaries, 34 Built-in Functions, 38 Regular Expressions with re.

print("This is an example of print function")
print('We\'re going to the store.')
print("Hi " + "there") #print Hi there
print("Hi",5) #print Hi 5
print("Hi +",5) #print Hi + 5
print(float("8.5") + 5) #print 13.5

"""
multiple
line
comments
"""

print(6/3) #print 2.0
print(6//3) #print 2
print(5/2) #print 2.5
print(5//2) #print 2
print(4**4) #print 256

exampleVar = 55 + 32
print(exampleVar) #print 87
xunpacking, yunpacking = (3,5)
print(xunpacking) #print 3
print(yunpacking) #print 5
print("\n")

condition = 1
while condition < 10:
	print(condition)
	condition += 1
makeupcondition = 1
while True:
	print("makeupcondition:", makeupcondition)
	makeupcondition += 1
	if makeupcondition == 5:
		break

exampleList = [1,5,6,1,6,7,8,9,345,53,5]
for eachnumber in exampleList:
	print(eachnumber)
for x in range(1,11):
	print(x,end="")  #print number 1 to 10 on one line
print("\n")

x = 5
y = 8
z = 5
a = 3
if x < y:
	print("x is less than y")
if z < y > x:
	print("y is greater than z and greater than x")
if z < y > x > a:
	print("y is greater than z and greater than x, and y greater than a")
if z <= x:
	print("z is less than or equal to x")
if z == x:
	print("z is equal to x")
if z != y:
	print("z is not equal to y")

x = 5
y = 8
if x > y:
	print("x is greater than y")
else:
	print("x is not greater than y")

x = 5
y = 10
z = 22
if x > y:
	print("x is greater than y")
elif x < z:
	print("x is less than z")
elif 5 > 2:
	print("5 is greater than 2") #5 is greater than 2 is not printed because x is less than z was the first true which exits the if statement
else:
	print("if and elif(s) never ran")

def example():
	print("basic function")
	z = 3 + 9
	print(z)
example() #return basic function\n 12

def simple_addition(num1, num2):
	answer = num1 + num2
	print("num1 is",num1)
	print(answer)
simple_addition(5,3) #return num1 is 5\n 8
simple_addition(3,5) #return num1 is 3\n 8
simple_addition(num2=3,num1=5) #return num1 is 5\n 8

def simple(num1, num2=5):
	print(num1, num2)
simple(2) #return 2 5
def basic_window(width, height, font="times new roman", backgroundcolor = "white",scrollbar=True):
	print(width, height, font, backgroundcolor)
basic_window(500,350) #return 500 350 times new roman white
basic_window(500,350,"arial") #return 500 350 arial white
basic_window(500,350,backgroundcolor="black") #return 500 350 times new roman black

x = 6
def example():
	z = 5
	print(z)
	print(x)
	print(x + 6)
	#x+=6 #UnboundLocalError: local variable 'x' referenced before assignment.  x is not a global variable.  To solve the global variable problem., type global x below function declaration.
example() #return 5\n 6\n 12
def exampleglobal():
	global x
	print(x)
	x+=5
	print(x)
exampleglobal() #return 6\n 11
x = 6
def exampleglobal2():
	globalx = x #globalx is a local variable
	print(globalx)
	globalx+=5
	print(globalx)
exampleglobal2() #return 6\n 11
print("\n")
x = 6
def exampleglobal3():
	globalx = x #globalx is a local variable
	print(globalx)
	globalx+=5
	return globalx #return globalx statement returns 11 from global +=5
print(exampleglobal3()) #print 6\n 11
#or
x = exampleglobal3()
print(x) #print 6\n 11

text = "Sample Text to Save\nNew line!"
saveFile = open("exampleFile.txt","w") #w-->write r-->read a-->append.  Can specify a file path.
saveFile.write(text)
saveFile.close() #must close().  Close file or file stays open.

appendMe = "\nNew bit of information"
appendFile = open("exampleFile.txt","a")  #w-->write r-->read a-->append.  Can specify a file path.
appendFile.write(appendMe)
appendFile.close() #must close().  Close file or file stays open.

readMe = open("exampleFile.txt","r").read() #w-->write r-->read a-->append.  Can specify a file path.
print(readMe) #print Sample Text to Save\n New line!\n New bit of information
readMeLines = open("exampleFile.txt","r").readlines() #w-->write r-->read a-->append.  Can specify a file path.
print(readMeLines) #print ['Sample Text to Save\n', 'New line!\n', 'New bit of information']

# Instructor taught the basic classes
class calculator:
	def addition(x,y):
		added = x + y
		print(added)
	def subtraction(x,y):
		sub = x - y
		print(sub)
	def multiplication(x,y):
		mult = x * y
		print(mult)
	def division(x,y):
		div = x / y
		print(div)
calculator.multiplication(3,5) #return 15
calculator.addition(5,2) #return 7
calculator.subtraction(10,9) #return 1

import epicthing
epicthing.epic()
#importing the module it runs through the module to load like loading a function.  Loads in order.
#if we commented epicthing.epic() statement, then import epicthing returns epicthing first line
#if we uncommented epicthing.epic statement, then we return epicthing first line\nRead epicthing file epic() function print statement
#However, the statement in epicthing.py if __name__ == "__main__": allows us to return epicthing first line\nRead epicthing file epic() function print statement only.

# x = input("What is your name? ")
# print("Hello " +x)

import statistics
example_list = [4,6,2,6,7,8,2,5,6,78,4,6,7,2,2,2]
x = statistics.mean(example_list)
print(x) #print 9.1875
y = statistics.median(example_list)
print(y) #print 5.5
z = statistics.mode(example_list)
print(z) #print 2
print("mode() error message when there are two numbers appearing same equal times")
a = statistics.stdev(example_list)
print(a) #print 18.468779963314667
b = statistics.variance(example_list)
print(b) #print 341.09583333333336

#in my Linux ubuntu, to view Python import modules, in Linux file explorer, the path is usr/lib/python3.5.  Open a module .py file in Sublime Text to read the module .py file.  For example, to view import statistics or statistics module, open statistics.py file and search for a module command such as mean def mean and median def median.  I discovered _sum which is used in variable c below.  These are the vanilla import modules standard when installing python3.5.
example_list = [4,6,2,6,7,8,2,5,6,78,4,6,7,2,2,2]
import statistics as s
c = s._sum(example_list)
print(c) #print (<class 'int'>, Fraction(147, 1), 16) 147 sum, 16 count
from statistics import median_high
d = median_high([1, 3, 5])
e = median_high([1, 3, 5, 7]) #BTW, there is a media_low
f = statistics.median([1, 3, 5, 7])
print(d) #print 3
print(e) #print 5
print(f) #print 4.0
from statistics import median_low as ml
g = ml([1, 3, 5, 7])
print(g) #print 3
from statistics import variance, mean as m
print(variance(example_list)) #print 341.09583333333336
print(m(example_list)) #print 9.1875
from statistics import *
print(median(example_list)) #print 5.5
print(mode(example_list)) #print 2

#A module is a Python script.  The module below is for makingmodules.py
def examplemodule(data):
	print(data)

def exampleFunc():
	return 15, 6 #<-- tuple
x,y = exampleFunc()
print(x) #print 15
print(y) #print 6
x = 5, 7, 2, 6 #<-- tuple
print(x[1]) #print 7
x = (5, 7, 2, 6)
print(x[1]) #print 7
print(x[1],x[2]) #print 7 2

x = [5, 6, 2, 1, 6, 7, 2, 2, 6, 7, 2]
x.append(2)
print(x) #print [5, 6, 2, 1, 6, 7, 2, 2, 6, 7, 2, 2]
x.insert(2,99)
print(x) #print [5, 6, 99, 2, 1, 6, 7, 2, 2, 6, 7, 2, 2]
x.remove(2)
print(x) #print [5, 6, 2, 1, 6, 7, 2, 2, 6, 7, 2, 2]
print(x[5]) #print 7
print(x[5:7]) #print [7,2]
print(x[5:9]) #print [7,2,2,6]
print(x[-1]) #print 2
print(x[-3]) #print 7
print(x.index(1)) #print 3
print(x.count(6)) #print 3
x.sort() #sort is a function run on the list.  Lists are mutable.  Changing the list.
print(x) #print [1, 2, 2, 2, 2, 5, 6, 6, 6, 7, 7, 99]
# side for loop with .count()
# x = [5, 6, 2, 1, 6, 7, 2, 2, 6, 7, 2]
# for number in range(1,11):
# 	print("number",number,"in x list:",x.count(number))
y = ["janet","jessy","kelly","alice","joe","bob"]
y.sort()
print(y) #print ['alice', 'bob', 'janet', 'jessy', 'joe', 'kelly']

x = [[5, 6], [6, 7], [7,2], [2,5]]
print(x) #print [[5, 6], [6, 7], [7, 2], [2, 5]]
print(x[1]) #print [6, 7]
print(x[1][0]) #print 6
xmultidimensionallist = [
[[5,7],[6,6]],[[6,6],[7,8]],[7,2],[2,5]
]
#easier ways to view multi-dimensional lists
multidimensionallist = [
[
[5,7],[6,6]],
[[6,6],[7,8]],
[7,2],
[2,5]
]
print(multidimensionallist[0][0][1]) #prints 7
print(multidimensionallist[1][0][0]) #prints 6
print(multidimensionallist[3][1]) #prints 5

import csv
with open("example.csv") as csvfile:
	readCSV = csv.reader(csvfile, delimiter=",")
	dates = []
	colors = []
	for row in readCSV:
		print(row) #print ['1/2/2014', '5', '8', 'red']\n ['1/3/2014', '5', '2', 'green']\n ['1/4/2014', '9', '1', 'blue'].  Note numbers and dates are returned in string.		
	print(row[0]) #print 1/4/2014 because the last row from for row in readCSV statement is ['1/4/2014', '9', '1', 'blue']
	print(row[0],row[1]) #print 1/4/2014 9 because the last row from for row in readCSV statement is ['1/4/2014', '9', '1', 'blue']
	print(row[3]) #print blue
with open("example.csv") as csvfile:
	readCSV = csv.reader(csvfile, delimiter=",")
	dates = []
	colors = []
	for row2 in readCSV:
		date = row2[0]
		color = row2[3]
		dates.append(date)
		colors.append(color)
	print(dates) #prints ['1/2/2014', '1/3/2014', '1/4/2014']
	print(colors) #prints ['red', 'green', 'blue']
	
	# whatColor = input("What color do you wish to know the date of? ")
	# colorindex = colors.index(whatColor.lower())
	# theDate = dates[colorindex]
	# print("The date of "+whatColor+" is "+theDate+".")

	# try:
	# 	whatColor = input("What color do you wish to know the date of? ")
	# 	colorindex = colors.index(whatColor.lower())
	# 	theDate = dates[colorindex]
	# 	print("The date of "+whatColor+" is "+theDate+".")
	# except Exception as e:
	# 	print(e) #print '*color*' is not in list which is the ValueError: *color*' is not in list.  BTW, except ValueError as e: also works for the except statement
	# print("continuing") #print continuing
	try:
		whatColor = input("What color do you wish to know the date of? ")
		if whatColor in colors:
			colorindex = colors.index(whatColor.lower())
			theDate = dates[colorindex]
			print("The date of "+whatColor+" is "+theDate+".")
		else:
			print("Color not found or is not a color")
	except Exception as e:
		print(e) #print '*color*' is not in list which is the ValueError: *color*' is not in list.  BTW, except ValueError as e: also works for the except statement
	print("continuing") #print continuing

print("""

So this is a simple
multi-line
print, pretty cool, huh? or eh?

===========
|         |
|         |
|         |
|         |
|         |
===========
""")

exDictionary = {"Jack":15, "Bob":22, "Alice":12, "Kevin": 17}
print(exDictionary) #print {'Bob': 22, 'Kevin': 17, 'Jack': 15, 'Alice': 12}
print(exDictionary["Jack"]) #print 15
exDictionary["Tim"] = 14
print(exDictionary) #print {'Bob': 22, 'Tim': 14, 'Kevin': 17, 'Jack': 15, 'Alice': 12}
exDictionary["Tim"] = 15
print(exDictionary) #print {'Bob': 22, 'Tim': 15, 'Kevin': 17, 'Jack': 15, 'Alice': 12}
del exDictionary["Tim"]
print(exDictionary) #print {'Bob': 22, 'Kevin': 17, 'Jack': 15, 'Alice': 12}
exDictionary = {"Jack":[15,"blonde"], "Bob":[22,"brown"], "Alice":[12,"black"], "Kevin":[17,"ginger"]}
print(exDictionary) #print {'Kevin': [17, 'ginger'], 'Bob': [22, 'brown'], 'Jack': [15, 'blonde'], 'Alice': [12, 'black']}
print(exDictionary["Jack"]) #print [15, 'blonde']
print(exDictionary["Jack"][1]) #print blonde

exampleNumber1 = -5
exampleNumber2 = 5
print(abs(exampleNumber1)) #print 5
print(abs(exampleNumber2)) #print 5
if abs(exampleNumber1) == exampleNumber2:
	print("These numbers are the same")

#help() #1. run help().  See help>  2.  Type a python command; e.g. print.  Information displayed.  Press page up and page down.  3.  Type q to quit.  4.  Type ctrl+c to quit.  Perhaps create a help.py file to run help() only?

exampleListNumbers = [5,2,6,7,8,0]
print(max(exampleListNumbers)) #print 8
print(min(exampleListNumbers)) #print 0

x = 5.622
print(round(x)) #print 6
x = 5.222
print(round(x)) #print 5
import math
print(math.floor(x)) #print 5
print(math.ceil(x)) #print 6

intMe = "55"
print(type(intMe)) #print <class 'str'>
print(int(intMe) + 10) #print 65
print(float(intMe)) #print 55.0
print(float(intMe) + .9) #print 55.9

#regular expressions is its own programming knowledge.  It's pass a string of arguments to apply to a string of text.  e.g. Have a paragraph.  Pull off or I want names and ages only.
"""
Identifiers

\ this is a character, please pay attention
\d any number
\D anything except a number
\s space
\S anything except a space
\w any character
\W anything except a character
. any character except for a new line
\b the white space around words
\. a period

Modifiers

{1,3} we're expecting 1-3.  \d{1-3}
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the ending of a string
^ Match the beginning of a string
| either or.  \d{1-3} | \w{5-6}
[] range or variance [A-Za-z] [1-5a-qA-Z]<--not 1-5, then a-q, then A-Z.  It's any of the following.
{x} expecting "x" amount

White Space Characters

\n new line
\s space
\t tab
\e escape
\f form feed
\r return or carriage return

Don't Forget

. + * ? { } $ ^ ( ) { } | \ all must be escaped

"""

import re
exampleString = """
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
"""
ages = re.findall(r"\d{1,3}",exampleString)
names = re.findall(r"[A-Z][a-z]*",exampleString)
print(ages) #print ['15', '27', '97', '102']
print(names) #print ['Jessica', 'Daniel', 'Edward', 'Oscar']
ageDict = {}
print(ageDict)
x = 0
for eachName in names:
	ageDict[eachName] = ages[x]
	x += 1
print(ageDict) #print {'Oscar': '102', 'Daniel': '27', 'Jessica': '15', 'Edward': '97'}
#instructor says he uses re.findall() most of the time