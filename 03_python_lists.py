#In this file we will look at lists, dictionaries, set, tuples, range.

#Lists
myList = [1, 2, 3, 4, 5]
print(myList)

print(type(myList)) # <class 'list'>

#Grab the first object of the list

print(myList[0]) # 1

#How many objects are in the list?

print(f"Our list object Mylist has {len(myList)} elements.") 

#Nice thing about lists: they are flexible with respect to the data type

mixedList = [1, "two", 3.0, [4, 'four'], True]

#We can add and remove objects from a list

mixedList.append(6)

print(mixedList)

#Removing

mixedList.pop() #Without an argument removes the last item

print(mixedList)

#How many times does the integer 1 appear?
print(mixedList.count(1))

#Reverse a list
mixedList.reverse()
print(mixedList)
