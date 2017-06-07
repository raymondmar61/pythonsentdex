 #sentdex
 #Video 30 Python 3 Reading from a CSV spreadsheet
 #Video 31 Python 3 Try and Except error Handling
 #Video 32 Python 3 Multi-line Print

import csv
with open("example.csv") as csvfile:
	readCSV = csv.reader(csvfile,delimiter=",")
	for row in readCSV:
		print(row) #returned ['1/2/2014', '5', '8', 'red'] \n ['1/3/2014', '5', '2', 'green'] \n ['1/4/2014', '9', '1', 'blue'].  Returned each line in its individual list as a string?
		print(row[0]) #returned 1/2/2014 \n 1/3/2014 \n 1/4/2014		
		print(row[0],row[1]) #returned 1/2/2014 5 \n 1/3/2014 5 \n 1/4/2014 9
print("\n")

with open("example.csv") as csvfile:
	readCSV = csv.reader(csvfile,delimiter=",")
	dates = []
	colors = []
	for row in readCSV:
		color = row[3]
		date = row[0]
		dates.append(date)
		colors.append(color)
	print(dates) #prints ['1/2/2014', '1/3/2014', '1/4/2014']
	print(colors) #prints ['red', 'green', 'blue']

whatColor = input("What color do you wish to know the date of? ")
colorindex = colors.index(whatColor.lower()) #get index number of colors list
theDate = dates[colorindex]
print("The date of " +whatColor, "is" ,dates[colorindex]) #prints The date of ReD is 1/2/2014 if colorindex = ReD
print("\n")

try:
	whatColor = input("What color do you wish to know the date of? ")
	colorindex = colors.index(whatColor.lower()) #get index number of colors list
	theDate = dates[colorindex]
	print("The date of " +whatColor, "is" ,dates[colorindex]) #prints The date of ReD is 1/2/2014 if colorindex = ReD
except Exception as e:
	print(e) #prints 'pink' is not in list if whatColor = pink
print("continuing")
print("\n")

try:
	whatColor = input("What color do you wish to know the date of? ")
	if whatColor in colors:
		colorindex = colors.index(whatColor.lower()) #get index number of colors list
		theDate = dates[colorindex]
		print("The date of " +whatColor, "is" ,dates[colorindex]) #prints The date of ReD is 1/2/2014 if colorindex = ReD
	else:
		print(whatColor, "not found or is not a color!") #prints pink not found or is not a color! if colorindex = pink
except NameError as e:
	print(e)
print("continuing")
print("\n")

print("Line 1 \nLine 2 \nLine 3")
print("""Line 4
Line 5
Line 6*no blank line*""")
print("""*blank line 1*
*blank line 2*
So this is a simple
mutli-line
print.  Pretty cool, huh! or eh?
""")