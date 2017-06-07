#sentdex
#Video 35 Python 3 OS Module

import os
currentdirectory = os.getcwd() #get current working directory
print(currentdirectory) #prints /home/mar/Python/sentdex
os.mkdir("tempnewdirectory") #make directory folder named tempnewdirectory
import time
time.sleep(3)
os.rmdir("tempnewdirectory") #delete directory folder named tempnewdirectory

os.mkdir("newDir1")
time.sleep(3)
os.rename("newDir1","newDir2")
time.sleep(3)
os.rmdir("newDir2")
