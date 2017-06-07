 #sentdex
 #Video 27 Python 3 Lists and Tuples
 #Video 28 Python 3 List Manipulation
 #Video 29 Python 3 Multi-dimensional List

 #lists are mutable.  Can change.  Surround by brackets []
 #tuples are immutable.  Can't change.  Surround by paranthesis () or nothing; for example (5,6,2,6) or 5,6,2,6 without paranthesis.

x = 5,6,2,6
y = [5,6,2,6]
print(x[1]) #print 6
print(y[2]) #print 2
print(y[2], y[3]) #print 2 6
print("\n")

x = [5,6,2,1,6,7,2,2,6,7,2]
x.append(2)
print(x) # prints [5, 6, 2, 1, 6, 7, 2, 2, 6, 7, 2, 2]
x.insert(2,99) #the econd element number 9 is inserted at second position
print(x) # prints [5, 6, 99, 2, 1, 6, 7, 2, 2, 6, 7, 2, 2]
x.remove(2) #deletes the first number 2
print(x) # prints [5, 6, 99, 1, 6, 7, 2, 2, 6, 7, 2, 2]
x.remove(x[2]) #removes element number 2 or the third position character
print(x) #prints [5, 6, 1, 6, 7, 2, 2, 6, 7, 2, 2]
print(x[5]) #prints the six position 2
print(x[5:9]) #prints the six position 2, seventh position 2, eigth position 6, and ninth position 7.
print(x[-1]) #prints the 2 at the end of the list
print(x) #prints [5, 6, 1, 6, 7, 2, 2, 6, 7, 2, 2]
print(x.index(1)) #prints 2 which is the index value of the number 1
print(x.count(6)) #prints 3 which is counting how many 6 is in the list
x.sort()
print(x) #prints [1, 2, 2, 2, 2, 5, 6, 6, 6, 7, 7]

y = ["Janet","Jessy","Kelly","Alice","Joe","Bob"]
y.sort()
print(y) #['Alice', 'Bob', 'Janet', 'Jessy', 'Joe', 'Kelly']
print("\n")

xonedimensionallist = [5,6,7,2]
xtwodimensionallist = [[5,6],[6,7],[7,2],[2,5]]
print(xtwodimensionallist) #prints [[5, 6], [6, 7], [7, 2], [2, 5]]
print(xtwodimensionallist[1]) #prints [6,7]
print(xtwodimensionallist[1][0]) #prints 6
xmultidimensionallist = [[[5,7],[6,6]],[[6,6],[7,8]],[7,2],[2,5]]
print(xmultidimensionallist) #prints [[[5, 7], [6, 6]], [[6, 6], [7, 8]], [7, 2], [2, 5]]
print(xmultidimensionallist[1][0][0]) #prints 6
#easier ways to view multi-dimensional lists
xmultidimensionallist = [
[[5,7],[6,6]],[[6,6],[7,8]],[7,2],[2,5]
]
multidimensionallist = [
[[5,7],[6,6]],
[[6,6],[7,8]],
[7,2],[2,5]
]
print(multidimensionallist[0][0][1]) #prints 7
print(multidimensionallist[3][1]) #prints 5