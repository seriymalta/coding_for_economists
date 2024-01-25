# Let's talk about functions

#Function definition syntax
def add_one(num):
  return num + 1

print(add_one(5))

# Function without return statement and without arguments
def add_one_str():
  print(6)

print(add_one_str())

#Try to assign the output of the function to a variable

res = add_one(5)
res_str = add_one_str()

print(res, res_str)

# Multiple return values
def add_one_return_both (num1):
  return num1, num1 + 1

print(add_one_return_both(5))

print(type(add_one_return_both(5)))

# More than one argument in functions
def add_two_nums(num1, num2):
  res = num1 + num2
  return num1, num2, res

print(add_two_nums(6,7))

# Default values for function arguments
def exponentiate(num, exponent=2):
  return num**exponent

print(exponentiate(5,3))
print(exponentiate(5, 2) == exponentiate(5))

# Keyword arguments: using the argument name to assign a value: here, order does not matter
print(exponentiate(exponent = 1, num = 2))

# Functions with variable number of arguments
def add_nums(*nums):
  res = 0

  for num in nums:
    res += num
  return res

print(add_nums(1, 2, 3, 4, 5, 6))

# Functions with variable number of keyword arguments
def add_nums_with_kwargs(**kwargs):
  res = 0
  for num in kwargs.values():
    res += num
  return res

print(add_nums_with_kwargs(num1 = 1, num2 = 2, num3 = 3))

# Let's try to code up some docstrings for a function

def cast_listitems_to_str(list_of_objects):
  """
  Casts all items in a list to a list of string.

  Parameters:
  ------------------------
  list_of_objects: list

  Returns:
  -----------------------
  
  
  """
  mylist = []
  for i in range(len(list_of_objects)):
    x = str(i)
    mylist.append(x)
  return mylist

print(cast_listitems_to_str([1, 2, 3, '5']))

#print(help(cast_listitems_to_str)) - to get help

# Scope of a variable 
def test(a, b):
  c = a + b # Scope of 'c' is confined to function
            #'c' is said to have local scope

c = 5 # Here, 'c' has global scope

# Lambda functions (aka anonymous functions)
# Reference function
def square(x):
  """
  
  Returns the square of a number.

  Parameters:
  ----------------------
  x: int or float or double

  Returns:
  -------------------------------
  square_x: int or float or double
  
  """
  return x**2

# Equivalent lambda function
square_lambda = lambda x: x**2

# Compare output
print(square(5) == square_lambda(5))