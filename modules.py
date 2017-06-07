#sentdex
#Video 24 Python 3 Statistics (Mean, Standard Deviation)
#Video 25 Python 3 Module Import Syntax
#Video 26 Python 3 Making Modules

import statistics
example_list = [4, 6, 2, 6, 7, 8, 2, 5, 6, 8, 4, 6, 7, 2, 2, 2]

meanx = statistics.mean(example_list)
print(meanx) #prints 4.8125
medianx = statistics.median(example_list)
print(medianx) #prints 5.5
modex = statistics.mode(example_list)
print(modex) #prints 2
print("mode() error message when there are two numbers appearing same equal times")
standarddeviationx = statistics.stdev(example_list)
print(standarddeviationx) #prints 2.2573952541221782
variancex = statistics.variance(example_list)
print(variancex) #prints 5.095833333333333

#syntax short hand way import a module as something
import statistics as s
print(s.mean(example_list)) #prints 4.8125

#syntax short hand way import a specific built-in function from a module
from statistics import variance
print(variance(example_list)) #prints 5.095833333333333

#syntax short hand way import a specific built-in function from a module as something
from statistics import variance as v
print(v(example_list)) #prints 5.095833333333333

#syntax short hand way import specific built-in functions from a module as somethings
from statistics import variance as v, mean as m
print(v(example_list)) #prints 5.095833333333333
print(m(example_list)) #prints 4.8125

#syntax short hand way import everything without typing "statistics."
from statistics import *
print(variance(example_list)) #prints 5.095833333333333
print(mean(example_list)) #prints 4.8125

#A module is a Python script
def examplemodule(data):
	print(data)