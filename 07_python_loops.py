# Let's have a look at loop syntax

# for loop operate on "iterables"

#Let's create an iterable object
myList = [1, 2, 'abc']

#Let's iterate over the object
for banana in myList:
  #Loop body needs to be indented once
  if banana == 1:
    print(banana)
  else:
    print("item not equal to 1.")

#Looping over a range of values

print("Using range(5)")
for i in range(5): #range () generates value on the fly
  print(i)

#Another way to do it
range_vals = [0, 1, 2, 3, 4] #Not memory efficient
print ("Using a list to display values 0-4")
for i in range_vals:
  print(i)

# Looping over list of strings and nesting loops
for name in ["James", "Jenny", "Jim"]:
  print(name)
  # Iterate through each string
  for letter in name:
    print(letter)

# Using the enumerate() function to get both index and value
print("Using enumerate()")
for index, name in enumerate(["James", "Jenny", "Jim"]):
  print(index, name)

#Equivalent loop using indexing
print("Using range() and indexing")
myList = ["James", "Jenny", "Jim"]
for index in range(len(myList)): #range(3)
  print(index, myList[index])

#Use a loop to create a list of capital letters from A-Z
print("Using a loop to create a list of capital letters from A-Z")
alphabet = []
for letter in range(65,91):
  print(letter,chr(letter))
  alphabet.append(chr(letter))
print(alphabet)

# While loops
# While loops are used when you don't know how many times you want to loop
print("While loop")
i = 0
while i < 10:
  print(i)
  i += 1

# While loop with break
print("While loop with break")
i = 0
while i < 10:
  print(i)
  if i == 5:
    break
  i += 1

# List cmoprehensions

# List comprehensions are a way to create a list in a single line of code

#Let's have a look at a for loop creating a list of squares from 0 to 10
squares = []
for num in range(0,11):
  squares.append(num**2)
print(squares)

#Doing the smae using list comprehension
squares = [num**2 for num in range(0,11)]
print(squares)

#Using if statements in list comprehensions
even_squares = [num**2 for num in range(0,11) if num % 2 == 0]
print(even_squares)