#Sentdex
#Video 37 Python 3 urllibmodule
#Video 38 Python 3 Regular Expressions Regex with re
#Video 39 Python 3 Parsing Websites with re and urllib
#access the internet via Python

import urllib.request
import urllib.parse

# x = urllib.request.urlopen("https://www.google.com")
# print(x.read()) #prints source code of the website

#post request trivia ? is first variable & is subsequent variable
url = "http://pythonprogramming.net"
values = {"s":"basic","submit":"Search"}
data = urllib.parse.urlencode(values)
data = data.encode("utf-8")
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
responseData = response.read()
print(responseData)