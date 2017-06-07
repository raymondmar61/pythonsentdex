 #sentdex
 #Video 33 Python 3 Dictionaries

#Dictionary entry-->key:value.  Printing a dictionary order is random.
exDict = {"Jack":15, "Bob":22, "Alice":12, "Kevin":17}
print(exDict) #prints {'Bob': 22, 'Kevin': 17, 'Jack': 15, 'Alice': 12}
print(exDict["Jack"]) #prints 15
exDict["Tim"] = 14
print(exDict) #prints {'Tim': 14, 'Alice': 12, 'Kevin': 17, 'Jack': 15, 'Bob': 22}
exDict["Tim"] = 15
print(exDict) #prints {'Tim': 15, 'Alice': 12, 'Kevin': 17, 'Jack': 15, 'Bob': 22}
del exDict["Tim"]
print(exDict) #prints {'Bob': 22, 'Jack': 15, 'Alice': 12, 'Kevin': 17}
exDict = {"Jack":[15,"blonde"], "Bob":[22,"brown"], "Alice":[12,"black"], "Kevin":[17,"red"]}
print(exDict) #prints {'Alice': [12, 'black'], 'Kevin': [17, 'red'], 'Bob': [22, 'brown'], 'Jack': [15, 'blonde']}
print(exDict["Jack"]) #prints [15, 'blode']
print(exDict["Jack"][0]) #prints 15
print(exDict["Jack"][1]) #prints blonde