import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

if num1 != num2 and num1 < num2:
    print("num1 is not equal to num2 and num1 is less than num2")
else:
    print("Conditions not met")

import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

if num1 < num2:
    print("num1 is less than num2")

if num1 > num2:
    print("num1 is greater than num2")