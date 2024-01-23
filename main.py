import random

#Generate random integer number between 1 and 10
random_number = random.randint(20,34)
print(random_number) #We get a different integer every time we run the program

# First look at conditional statements
if random_number < 25:
  print("The number is less than 25")
elif random_number < 30:
  print("The number is less than 30")
else:
  print("The number is less than or equal to 34")

#Only the first if statement is evaluated
#Cases should typically be exhausted

#Nested if statements

a = random.randint(0,10)
b = random.randint(10,20)

if a < 9:
  print(f"a is less than 9.")
  if b < 19: #Only gets evaluated if a < 9
    print (f"b is smaller than 19.")

#Equivalently, we can combine the logical conditions
if a < 9 and b < 19:
  print("a is less than a and b is less than 19")