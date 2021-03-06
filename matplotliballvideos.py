#Sentdex Matplotlib Tutorial 1 - Introduction and Line, 2 - Legends titles and labels, 3 bar charts and histograms, 4 - Scatter Plots, 5 - stack plots, 6 Pie Charts, 7 - loading data from files, 8 - getting data from the internet and 9 - converting data from the internet, 10 - basic customizations, rotating, 11 - handling unix time labels, 12 - more customization of colors and fills, 13 - spines and horizontal lines, 14 - candlestick OHLC graphs, 15 - styles, 16 - Live graphs, 17 - annotations and placing text, 18 - annotating last price to edge of matplotlib graph, 19 - subplots, 20 - implementing subplots to our stock chart, 21 - adding more indicator data to our charts
#matplotlib.org website information


#Press Zoom button.  Left mouse click zoom in.  Right mouse click zoom out.
import matplotlib.pyplot as plt
#plt.plot([1,2,3],[5,7,4]) #plt.plot(x,y) (1,5), (2,7), (3,4)
"""
#1 - Introduction and Line
x=[1,2,3]
y=[5,7,4]
x2=[1,2,3]
y2=[10,14,12]
plt.plot(x,y, label="firstlineforlegend")
plt.plot(x2,y2, label="secondlineforlegend")
"""
"""
#2 - Legends titles and labels
x=[2,4,6,8,10]
y=[6,7,8,2,4]
x2=[1,3,5,7,9]
y2=[7,8,2,4,2]
plt.bar(x,y, label="bar1forlegend", color="red")
plt.bar(x2,y2, label="bar2forlegend", color="cyan")
"""
"""
#3 - bar charts and histograms
populationages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
ids = [x for x in range(0,len(populationages))]
print(ids) #print [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
#plt.bar(ids, populationages)
"""
"""
#3 - bar charts and histograms
populationages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(populationages,bins, histtype="bar", rwidth=1.0)
"""
"""
#4 - Scatter Plots
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]
plt.scatter(x,y, label="skitscatforlegend", color="black", marker="x", s=100)
"""
"""
#5 stack plots
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
#6 Pie Charts
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
"""
#7 - loading data from files
import numpy as np
x,y = np.loadtxt("example2.csv", delimiter=",", unpack=True, dtype=np.int64) #dtype=np.int64 converts to integer
print(x) #print [ 1  2  3  4  5  6  7  8  9 10]
print(y) #print [5 3 4 7 4 3 5 7 4 4]
"""
"""
#8 - getting data from the internet
#9 - converting data from the internet
import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(formatdate,encoding="utf-8"):
	strconverter=mdates.strpdate2num(formatdate)
	def bytesconverter(bbytes):
		sstring = bbytes.decode(encoding)
		return strconverter(sstring)
	return bytesconverter
def graph_data(stock):
	stockpriceurl="https://www.quandl.com/api/v1/datasets/WIKI/"+stock+".csv?column=4&sort_order=asc&collapse=quarterly&trim_start=2012-01-01&trim_end=2015-12-31"
	sourcecode=urllib.request.urlopen(stockpriceurl).read().decode()
	print(sourcecode)
	splitsource=sourcecode.split("\n")
	del(splitsource[0]) #delete Date,Close the first list item
	del(splitsource[-1]) #delete null the last list item
	print(splitsource)
	dateclose, closeprice = np.loadtxt(splitsource,delimiter=",",unpack=True,converters={0: bytespdate2num("%Y-%m-%d")})
	print(dateclose)
	print(closeprice)
	plt.plot_date(dateclose,closeprice, label="default dots")	
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.title("title\ntitlenewline")
	plt.legend()
	plt.show() #show graph default dots
	plt.plot_date(dateclose,closeprice, "-", label="line chart denoated by hyphen")
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.title("title\ntitlenewline")
	plt.legend()
	plt.show() #show graph line chart denoated by hyphen"	
graph_data("AAPL")
"""
"""
#10 - basic customizations, rotating labels
import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(formatdate,encoding="utf-8"):
	strconverter=mdates.strpdate2num(formatdate)
	def bytesconverter(bbytes):
		sstring = bbytes.decode(encoding)
		return strconverter(sstring)
	return bytesconverter
def graph_data(stock):
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))  #ax stands for axis
	stockpriceurl="https://www.quandl.com/api/v1/datasets/WIKI/"+stock+".csv?column=4&sort_order=asc&collapse=quarterly&trim_start=2012-01-01&trim_end=2015-12-31"
	sourcecode=urllib.request.urlopen(stockpriceurl).read().decode()
	print(sourcecode)
	splitsource=sourcecode.split("\n")
	del(splitsource[0]) #delete Date,Close the first list item
	del(splitsource[-1]) #delete null the last list item
	print(splitsource)
	dateclose, closeprice = np.loadtxt(splitsource,delimiter=",",unpack=True,converters={0: bytespdate2num("%Y-%m-%d")})
	print(dateclose)
	print(closeprice)
	ax1.plot_date(dateclose,closeprice, "-", label="line chart denoated by hyphen")
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45) #45 degrees
	ax1.grid(True, color='green', linestyle="-", linewidth=5) #show grid lines green color hyphen linewidth is five
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.title("title\ntitlenewline")
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
	plt.show() #show graph line chart denoated by hyphen"	
graph_data("AAPL")
"""
"""
#12 - more customization of colors and fills
import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(formatdate,encoding="utf-8"):
	strconverter=mdates.strpdate2num(formatdate)
	def bytesconverter(bbytes):
		sstring = bbytes.decode(encoding)
		return strconverter(sstring)
	return bytesconverter
def graph_data(stock):
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))  #ax stands for axis
	stockpriceurl="https://www.quandl.com/api/v1/datasets/WIKI/"+stock+".csv?column=4&sort_order=asc&collapse=quarterly&trim_start=2006-01-01&trim_end=2016-12-31"
	sourcecode=urllib.request.urlopen(stockpriceurl).read().decode()
	print(sourcecode)
	splitsource=sourcecode.split("\n")
	del(splitsource[0]) #delete Date,Close the first list item
	del(splitsource[-1]) #delete null the last list item
	print(splitsource)
	dateclose, closeprice = np.loadtxt(splitsource,delimiter=",",unpack=True,converters={0: bytespdate2num("%Y-%m-%d")})
	print(dateclose)
	print(closeprice)
	ax1.plot_date(dateclose,closeprice, "-", label="line chart denoated by hyphen")	
	ax1.plot([],[], linewidth=5, label="loss", color="red",alpha=0.5)
	ax1.plot([],[], linewidth=5, label="gain", color="green",alpha=0.5)	
	#ax1.fill_between(dateclose,closeprice,0, alpha=0.3) #chart filled below line, alpha is fill transparency
	#ax1.fill_between(dateclose,closeprice,36, alpha=0.3) #chart filled below line, alpha is fill transparency, y=36  is the y coordinate where the baseline is like the horiztonal line at y=0.  Like purchased stock at 36, above 36 is profit, below 36 is loss.
	#ax1.fill_between(dateclose,closeprice,closeprice[0], alpha=0.3) #chart filled below line, alpha is fill transparency, y=first close price is the y coordinate where the baseline is like the horiztonal line at y=0.  Like purchased stock at first closed price, above is profit, below is loss.
	ax1.fill_between(dateclose,closeprice,closeprice[0], where=(closeprice > closeprice[0]), facecolor = "green", alpha=0.3) #alpha is fill transparency, fill is filled when the close price is greater than the first close price.  green fill transparency color.
	ax1.fill_between(dateclose,closeprice,closeprice[0], where=(closeprice < closeprice[0]), facecolor = "red", alpha=0.5) #alpha is fill transparency, fill is filled green when the close price is greater than the first close price.  red fill transparency color when the close price is less than the first close price.
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45) #45 degrees
	ax1.grid(True, color='green', linestyle="-", linewidth=1) #show grid lines green color hyphen linewidth is one
	ax1.xaxis.label.set_color("cyan")
	ax1.yaxis.label.set_color("red")
	ax1.set_yticks([0,25,50,75]) #y axis tick mark labels 0, 25, 50, 75
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.title(stock)
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
	plt.show() #show graph line chart denoated by hyphen"	
graph_data("EBAY")
"""
"""
#13 - spines and horizontal lines
import numpy as np
import urllib
import matplotlib.dates as mdates
def bytespdate2num(formatdate,encoding="utf-8"):
	strconverter=mdates.strpdate2num(formatdate)
	def bytesconverter(bbytes):
		sstring = bbytes.decode(encoding)
		return strconverter(sstring)
	return bytesconverter
def graph_data(stock):
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))  #ax stands for axis
	stockpriceurl="https://www.quandl.com/api/v1/datasets/WIKI/"+stock+".csv?column=4&sort_order=asc&collapse=quarterly&trim_start=2006-01-01&trim_end=2016-12-31"
	sourcecode=urllib.request.urlopen(stockpriceurl).read().decode()
	print(sourcecode)
	splitsource=sourcecode.split("\n")
	del(splitsource[0]) #delete Date,Close the first list item
	del(splitsource[-1]) #delete null the last list item
	print(splitsource)
	dateclose, closeprice = np.loadtxt(splitsource,delimiter=",",unpack=True,converters={0: bytespdate2num("%Y-%m-%d")})
	print(dateclose)
	print(closeprice)
	ax1.plot_date(dateclose,closeprice, "-", label="line chart denoated by hyphen")	
	ax1.plot([],[], linewidth=5, label="loss", color="red",alpha=0.5)
	ax1.plot([],[], linewidth=5, label="gain", color="green",alpha=0.5)
	ax1.axhline(closeprice[0], color="black", linewidth=5) #black horizontal line at the first close price
	ax1.axhline(50, color="black", linewidth=5) #black horizontal line at y=50
	ax1.fill_between(dateclose,closeprice,closeprice[0], where=(closeprice > closeprice[0]), facecolor = "green", alpha=0.3) #alpha is fill transparency, fill is filled when the close price is greater than the first close price.  green fill transparency color.
	ax1.fill_between(dateclose,closeprice,closeprice[0], where=(closeprice < closeprice[0]), facecolor = "red", alpha=0.5) #alpha is fill transparency, fill is filled green when the close price is greater than the first close price.  red fill transparency color when the close price is less than the first close price.
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45) #45 degrees
	ax1.grid(True, color='green', linestyle="-", linewidth=1) #show grid lines green color hyphen linewidth is one
	ax1.set_yticks([0,25,50,75]) #y axis tick mark labels 0, 25, 50, 75
	ax1.spines["left"].set_color("cyan") #color of left spine is cyan.   Spine is the line surrounding the chart.
	ax1.spines["right"].set_visible(False) #no right spine
	ax1.spines["top"].set_visible(False) #no top spine
	ax1.spines["left"].set_linewidth(5) #left spine is width 5
	ax1.tick_params(axis="x", colors="#f06215") #x labels color is orange
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.title(stock)
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
	plt.show() #show graph line chart denoated by hyphen"	
graph_data("EBAY")
"""
"""
#14 - candlestick OHLC graphs
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import numpy as np
import urllib
import random
def bytespdate2num(formatdate,encoding="utf-8"):
	strconverter=mdates.strpdate2num(formatdate)
	def bytesconverter(bbytes):
		sstring = bbytes.decode(encoding)
		return strconverter(sstring)
	return bytesconverter
def graph_data(stock):
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))  #ax stands for axis
	stockpriceurl="https://www.quandl.com/api/v1/datasets/WIKI/"+stock+".csv?column=4&sort_order=asc&collapse=quarterly&trim_start=2006-01-01&trim_end=2016-12-31"
	sourcecode=urllib.request.urlopen(stockpriceurl).read().decode()
	print(sourcecode)
	splitsource=sourcecode.split("\n")
	del(splitsource[0]) #delete Date,Close the first list item
	del(splitsource[-1]) #delete null the last list item
	print(splitsource)
	dateclose, closeprice = np.loadtxt(splitsource,delimiter=",",unpack=True,converters={0: bytespdate2num("%Y-%m-%d")})
	print(dateclose)
	print(closeprice)
	x=0
	y=len(dateclose)
	ohlc=[]
	while x < y:
		openprice = random.randint(30,50)
		highprice = random.randint(openprice+10,openprice+20)
		lowprice = random.randint(openprice-20,openprice-10)
		volume = random.randint(1000000,2000000)
		appendme = dateclose[x], openprice, highprice, lowprice, closeprice[x], volume
		ohlc.append(appendme)
		x+=1
	candlestick_ohlc(ax1, ohlc, width = 0.4, colorup="#77d879", colordown="#db3f3f")
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y)%m-%d"))
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(5)) #number of markes on x-axis
	ax1.grid(True)
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.title(stock)
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
	plt.show() #show graph line chart denoated by hyphen"	
graph_data("EBAY")
"""
"""
#15 - Styles
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style
import numpy as np
import urllib
import random
#style.use("ggplot")
style.use("fivethirtyeight")
print(plt.style.available) #print ['seaborn-paper', 'seaborn-dark', 'seaborn-poster', 'seaborn-whitegrid', 'fivethirtyeight', 'grayscale', 'ggplot', 'seaborn-notebook', 'seaborn-muted', 'seaborn-darkgrid', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-white', 'seaborn-ticks', 'seaborn-talk', 'seaborn-pastel', 'seaborn-deep', 'classic', 'seaborn-dark-palette', 'dark_background', 'bmh']
print(plt.__file__) #find the directory for the styles.  Open the style file to modify.
def bytespdate2num(formatdate,encoding="utf-8"):
	strconverter=mdates.strpdate2num(formatdate)
	def bytesconverter(bbytes):
		sstring = bbytes.decode(encoding)
		return strconverter(sstring)
	return bytesconverter
def graph_data(stock):
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))  #ax stands for axis
	stockpriceurl="https://www.quandl.com/api/v1/datasets/WIKI/"+stock+".csv?column=4&sort_order=asc&collapse=quarterly&trim_start=2006-01-01&trim_end=2016-12-31"
	sourcecode=urllib.request.urlopen(stockpriceurl).read().decode()
	print(sourcecode)
	splitsource=sourcecode.split("\n")
	del(splitsource[0]) #delete Date,Close the first list item
	del(splitsource[-1]) #delete null the last list item
	print(splitsource)
	dateclose, closeprice = np.loadtxt(splitsource,delimiter=",",unpack=True,converters={0: bytespdate2num("%Y-%m-%d")})
	print(dateclose)
	print(closeprice)
	x=0
	y=len(dateclose)
	ohlc=[]
	while x < y:
		openprice = random.randint(30,50)
		highprice = random.randint(openprice+10,openprice+20)
		lowprice = random.randint(openprice-20,openprice-10)
		volume = random.randint(1000000,2000000)
		appendme = dateclose[x], openprice, highprice, lowprice, closeprice[x], volume
		ohlc.append(appendme)
		x+=1
	#candlestick_ohlc(ax1, ohlc, width = 0.4, colorup="#77d879", colordown="#db3f3f")
	ax1.plot(dateclose,closeprice)
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y)%m-%d"))
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(5)) #number of markes on x-axis
	ax1.grid(True)
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.title(stock)
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
	plt.show() #show graph line chart denoated by hyphen"	
graph_data("EBAY")
"""
"""
#16 - Live graphs
import matplotlib.animation as animation
from matplotlib import style
style.use("fivethirtyeight")
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animate(i):
	graph_data = open("example.txt","r").read()
	lines = graph_data.split("\n")
	xcoordinates = []
	ycoordinates = []
	for line in lines:
		if len(line) > 1:
			x,y = line.split(",")
			xcoordinates.append(x)
			ycoordinates.append(y)
	ax1.clear()
	ax1.plot(xcoordinates,ycoordinates)
ani = animation.FuncAnimation(fig, animate, interval=1000) #interval in miliseconds 1000 miliseconds = 1 second.  Interval created to update chart when new coordinates are saved in example.txt.
plt.show()
"""
"""
#17 - annotations and placing text
#18 - annotating last price to edge of matplotlib graph
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import numpy as np
import urllib
import random
def bytespdate2num(formatdate,encoding="utf-8"):
	strconverter=mdates.strpdate2num(formatdate)
	def bytesconverter(bbytes):
		sstring = bbytes.decode(encoding)
		return strconverter(sstring)
	return bytesconverter
def graph_data(stock):
	fig = plt.figure()
	ax1 = plt.subplot2grid((1,1), (0,0))  #ax stands for axis
	stockpriceurl="https://www.quandl.com/api/v1/datasets/WIKI/"+stock+".csv?column=4&sort_order=asc&collapse=quarterly&trim_start=2006-01-01&trim_end=2016-12-31"
	sourcecode=urllib.request.urlopen(stockpriceurl).read().decode()
	print(sourcecode)
	splitsource=sourcecode.split("\n")
	del(splitsource[0]) #delete Date,Close the first list item
	del(splitsource[-1]) #delete null the last list item
	print(splitsource)
	dateclose, closeprice = np.loadtxt(splitsource,delimiter=",",unpack=True,converters={0: bytespdate2num("%Y-%m-%d")})
	print(dateclose)
	print(closeprice)
	x=0
	y=len(dateclose)
	ohlc=[]
	while x < y:
		openprice = random.randint(30,50)
		highprice = random.randint(openprice+10,openprice+20)
		lowprice = random.randint(openprice-20,openprice-10)
		volume = random.randint(1000000,2000000)
		appendme = dateclose[x], openprice, highprice, lowprice, closeprice[x], volume
		ohlc.append(appendme)
		x+=1
	candlestick_ohlc(ax1, ohlc, width = 0.4, colorup="#77d879", colordown="#db3f3f")
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)
	ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y)%m-%d"))
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(5)) #number of markes on x-axis
	ax1.grid(True)
	bboxprops = dict(boxstyle="larrow", facecolor="white", edgecolor="black", linewidth=1)
	ax1.annotate(str(closeprice[-1]), (dateclose[-1], closeprice[-1]),xytext = (dateclose[-1]+4,closeprice[-1]), bbox=bboxprops)
	#17 annotations and placing text
	# ax1.annotate("Big News",(dateclose[11],closeprice[11]),xytext=(0.8, 0.9), textcoords="axes fraction",arrowprops=dict(facecolor="grey",color="grey")) #80% of xaxis, 90% of yaxis location annotate with arrowprops create arrow at dateclose and closeprice twelevth each.  Index starts at zero.
	# fontdictionary = {"family": "serif", "color":"darkred", "size":15}
	# ax1.text(dateclose[10],closeprice[1], "Text on chart", fontdict=fontdictionary) #text located on eleventh dateclose and second closeprice.  Index starts at zero.
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.title(stock)
	#plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
	plt.show() #show graph line chart denoated by hyphen"	
graph_data("EBAY")
"""
"""
#19 - subplots
import random
from matplotlib import style
style.use("fivethirtyeight")
figure = plt.figure()
def create_plots():
	xs = []
	ys = []
	for i in range(20):
		x = i
		y = random.randrange(10)
		xs.append(x)
		ys.append(y)
	return xs, ys
#first way to create a subplot
ax01 = figure.add_subplot(111)
ax1 = figure.add_subplot(211)
ax2 = figure.add_subplot(221)
ax3 = figure.add_subplot(222)
ax4 = figure.add_subplot(212)
x, y = create_plots()
ax2.plot(x,y)
x, y = create_plots()
ax3.plot(x,y)
x, y = create_plots()
ax4.plot(x,y)
plt.show()
#second way to create a subplot
ax1subplottogrid = plt.subplot2grid((6,1),(0,0),rowspan=2,colspan=1) #6 rows, 1 columns.  Starting point is upper left.
ax2subplottogrid = plt.subplot2grid((6,1),(2,0),rowspan=3,colspan=1) #6 rows, 1 columns.  Starting point is upper left.
ax3subplottogrid = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1) #6 rows, 1 columns.  Starting point is upper left.
x, y = create_plots()
ax1subplottogrid.plot(x,y)
x, y = create_plots()
ax2subplottogrid.plot(x,y)
x, y = create_plots()
ax3subplottogrid.plot(x,y)
plt.show()
"""
#20 - implementing subplots to our stock chart
#21 - adding more indicator data to our charts
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import numpy as np
import urllib
import random
from matplotlib import style
style.use("fivethirtyeight")
movingaverage1 = 10
movingaverage2 = 30
def movingaverage(values, window):
	#using numpy
	weights = np.repeat(1.0, window)/window
	smas = np.convolve(values, weights, "valid")
	return smas
def highminuslow(highs,lows):
	return highs-lows
def bytespdate2num(formatdate,encoding="utf-8"):
	strconverter=mdates.strpdate2num(formatdate)
	def bytesconverter(bbytes):
		sstring = bbytes.decode(encoding)
		return strconverter(sstring)
	return bytesconverter
def graph_data(stock):
	fig = plt.figure()
	ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)  #ax stands for axis
	plt.title(stock)
	ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1)  #ax stands for axis
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)  #ax stands for axis
	stockpriceurl="https://www.quandl.com/api/v1/datasets/WIKI/"+stock+".csv?column=4&sort_order=asc&collapse=quarterly&trim_start=2006-01-01&trim_end=2016-12-31"
	sourcecode=urllib.request.urlopen(stockpriceurl).read().decode()
	print(sourcecode)
	splitsource=sourcecode.split("\n")
	del(splitsource[0]) #delete Date,Close the first list item
	del(splitsource[-1]) #delete null the last list item
	print(splitsource)
	dateclose, closeprice = np.loadtxt(splitsource,delimiter=",",unpack=True,converters={0: bytespdate2num("%Y-%m-%d")})
	print(dateclose)
	print(closeprice)
	x=0
	y=len(dateclose)
	ohlc=[]
	while x < y:
		openprice = random.randint(30,50)
		highprice = random.randint(openprice+10,openprice+20)
		lowprice = random.randint(openprice-20,openprice-10)
		volume = random.randint(1000000,2000000)
		appendme = dateclose[x], openprice, highprice, lowprice, closeprice[x], volume
		ohlc.append(appendme)
		x+=1
	mmovingaverage1 = movingaverage(closeprice,movingaverage1)
	mmovingaverage2 = movingaverage(closeprice,movingaverage2)	
	start = len(dateclose[movingaverage2-1:])
	#highlow = list(map(highminuslow, highprice, lowprice))
	#ax1.plot_date(dateclose,highlow,"-") #RM: can't get ax1 to plot
	candlestick_ohlc(ax2, ohlc, width = 0.4, colorup="#77d879", colordown="#db3f3f")
	for label in ax2.xaxis.get_ticklabels():
		label.set_rotation(45)
	ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y)%m-%d"))
	ax2.xaxis.set_major_locator(mticker.MaxNLocator(5)) #number of markes on x-axis
	ax2.grid(True)
	bboxprops = dict(boxstyle="larrow", facecolor="white", edgecolor="black", linewidth=1)
	ax2.annotate(str(closeprice[-1]), (dateclose[-1], closeprice[-1]),xytext = (dateclose[-1]+4,closeprice[-1]), bbox=bboxprops)
	#17 annotations and placing text
	# ax1.annotate("Big News",(dateclose[11],closeprice[11]),xytext=(0.8, 0.9), textcoords="axes fraction",arrowprops=dict(facecolor="grey",color="grey")) #80% of xaxis, 90% of yaxis location annotate with arrowprops create arrow at dateclose and closeprice twelevth each.  Index starts at zero.
	# fontdictionary = {"family": "serif", "color":"darkred", "size":15}
	# ax1.text(dateclose[10],closeprice[1], "Text on chart", fontdict=fontdictionary) #text located on eleventh dateclose and second closeprice.  Index starts at zero.
	#plt.legend()
	ax3.plot(dateclose[-start:],mmovingaverage1[-start:])
	ax3.plot(dateclose[-start:],mmovingaverage2[-start:])
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
	plt.show() #show graph line chart denoated by hyphen"	
graph_data("EBAY")


# x=[1,2,3]
# y=[5,7,4]
# x2=[1,2,3]
# y2=[10,14,12]
# plt.plot(x,y, label="firstlineforlegend")
# plt.plot(x2,y2, label="secondlineforlegend")
# plt.xlabel("xlabel")
# plt.ylabel("ylabel")
# plt.title("title\ntitlenewline")
# plt.legend()
# plt.show()