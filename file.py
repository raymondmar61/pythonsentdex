#sentdex
#Video 18 Python 3 Programming Tutorial - Writing to File
#Video 19 Python 3 Programming Tutorial - Appending Files
#Video 20 Python 3 Programming Tutorial - Read from a file

#Video 18 Python 3 Programming Tutorial - Writing to File
text = "Sample Text to Save\nNew line!"
saveFile = open("exampleFile.txt","w") #w=write, r=read, a=append.  If file doesn't exist, Python creates a new file with the name.  And file path can be typed out if the file is in another directory.
saveFile.write(text)
saveFile.close()

#Video 19 Python 3 Programming Tutorial - Appending Files
appendMe = "\nNew bit of information"
appendFile = open("exampleFile.txt","a") #w=write, r=read, a=append.  File path can be typed out if the file is in another directory.
appendFile.write(appendMe)
appendFile.close()

#Video 20 Python 3 Programming Tutorial - Read from a file
readMe = open("exampleFile.txt","r").read() #w=write, r=read, a=append.  File path can be typed out if the file is in another directory.
print(readMe) #print Sample Text to Save\n New line!\n New bit of information
readMeLines = open("exampleFile.txt","r").readlines()
print(readMeLines) #print ['Sample Text to Save\n', 'New line!\n', 'New bit of information']

