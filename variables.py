#Sentdex
#Video 14 Python 3 Programming Tutorial - Global and Local Variables
x = 6
def example():
	z = 5
	print(x, z)
	#x = x + 6 #error message UnboundLocalError: local variable 'x' referenced before assignment; in other words, x = 6 is not a global variable
example() #return 6 5

def exampleglobalvariable():
	global x
	z = 5
	x = x + 6
	print(x, z)
exampleglobalvariable() #return 12 5

x = 6
def exampleglobalvariable2():
	globalx = x #use when defining global variable is forbidden
	z = 5
	globalx = globalx + 6
	print(globalx, z)
exampleglobalvariable2() #return 12 5
print(x) #print 6.  The x = 6 is still x = 6, not x = 12 from exampleglobalvariable()

x = 6
def exampleglobalvariable3():
	globalx = x #use when defining global variable is forbidden
	z = 5
	globalx = globalx + 6
	return (globalx)
print(exampleglobalvariable3()) #print 12
print(x) #print 6.  The x = 6 is still x = 6, not x = 12 from exampleglobalvariable()