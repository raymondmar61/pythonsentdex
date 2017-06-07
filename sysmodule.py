#sentdex
#Video 36 Python 3 Sys Module

import sys
sys.stderr.write("This is stderr text\n")
sys.stderr.flush()
sys.stdout.write("This is stdout text\n")
print(sys.argv) #prints file name ['sysmodule.py']
#type python3.5 sysmodule.py "look at that!" at Linux command prompt, return ['sysmodule.py', 'look at that!']
if len(sys.argv) > 1:
	print(sys.argv[1]) #prints look at that!

#type python3.5 sysmodule.py 5.6 at Linux command prompt, return ['sysmodule.py', 5.6]
print(sys.argv)
if len(sys.argv) > 1:
	print(float(sys.argv[1])) #prints 5.6
	print(float(sys.argv[1]) + 5) #prints 10.6