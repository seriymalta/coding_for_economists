#First look at dictionaries

#Dictionaries are a data structure that can store multiple values in a single variable. 
#Dictionaries are written with curly brackets and have keys and values.

#Syntax:
#dictionary_name = {key1:value1, key2:value2, key3:value3}

myDict = {"Dog":"Barks", "Cat":"Meows", "Whale":"Shrieks"}
print(myDict)

#We cannot use the same indexing syntax as with lists/str
#print(myDict[0]) produces an error

print(myDict["Dog"])

#Getting the first key-value in a dictionary
print(list(myDict.items())[0])

print(len(myDict))
