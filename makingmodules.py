#sentdex
#Video 26 Python 3 Making Modules

#import examplemodule #error message--> No module named 'examplemodule'
import modules #modules is the Python file name modules.py in the same directory.  Python looks for modules in local folder, lib folder, and side packages or site packages.

modules.examplemodule("test")  #returns everything in modules.py and test.  examplemodule is the function in modules

import sentdexallvideos
sentdexallvideos.examplemodule("test2") #returns everything in sentdexallvideos.py and test2.  examplemodule is the function in sentdexallvideos
