#Sentdex Matplotlib Tutorial 1 - Introduction and Line, 2 - Legends titles and labels, 3 bar charts and histograms, 4 - Scatter Plots, 5 - stack plots, 6 Pie Charts, 7 - loading data from files, 


#Press Zoom button.  Left mouse click zoom in.  Right mouse click zoom out.
import matplotlib.pyplot as plt
#plt.plot([1,2,3],[5,7,4]) #plt.plot(x,y) (1,5), (2,7), (3,4)
"""
x=[1,2,3]
y=[5,7,4]
x2=[1,2,3]
y2=[10,14,12]
plt.plot(x,y, label="firstlineforlegend")
plt.plot(x2,y2, label="secondlineforlegend")
"""
"""
x=[2,4,6,8,10]
y=[6,7,8,2,4]
x2=[1,3,5,7,9]
y2=[7,8,2,4,2]
plt.bar(x,y, label="bar1forlegend", color="red")
plt.bar(x2,y2, label="bar2forlegend", color="cyan")
"""
"""
populationages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
ids = [x for x in range(0,len(populationages))]
print(ids) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
#plt.bar(ids, populationages)
"""
"""
populationages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(populationages,bins, histtype="bar", rwidth=1.0)
"""
"""
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]
plt.scatter(x,y, label="skitscatforlegend", color="black", marker="x", s=100)
"""
"""
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]
#plt.stackplot(days,sleeping,eating,working,playing, colors=["magenta","cyan","red","black"], label="legend label") #plot.stackplot(x,y1,y2,y3,yn)
#label="legend label" invalid for stackplot.  Need extra steps plt.plot() for each y category
plt.plot([],[],color="magenta", label="Sleeping", linewidth=5)
plt.plot([],[],color="cyan", label="Eating", linewidth=5)
plt.plot([],[],color="red", label="Working", linewidth=5)
plt.plot([],[],color="black", label="Playing", linewidth=5)
plt.stackplot(days,sleeping,eating,working,playing, colors=["magenta","cyan","red","black"]) #plot.stackplot(x,y1,y2,y3,yn)
"""
"""
slices=[7,2,2,13]
activities=["sleeping","eating","working","playing"]
piecolors = ["cyan","magenta","red","black"]
plt.pie(slices,labels=activities, colors=piecolors, startangle=90, shadow=True, explode=(0,0.1,0,0), autopct="%1.1f%%") #plot counterclockwise, explode extracts a pie piece from chart, autopct adds percentages
"""
"""
x=[]
y=[]
import csv
with open("example2.csv","r") as csvfile:
	plots = csv.reader(csvfile, delimiter=",")
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))
print(x) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(y) #print [5, 3, 4, 7, 4, 3, 5, 7, 4, 4]
"""
import numpy as np
x,y = np.loadtxt("example2.csv", delimiter=",", unpack=True, dtype=np.int64) #dtype=np.int64 converts to integer
print(x) #print [ 1  2  3  4  5  6  7  8  9 10]
print(y) #print [5 3 4 7 4 3 5 7 4 4]
plt.plot(x,y, label="linechartx's_and_y's")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("title\ntitlenewline")
plt.legend()
plt.show() #show graph