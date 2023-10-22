


#1

"""import  random


def x():
    return random.randint(1,6)


while True:
    dice = x()
    print("The each roll is: ", dice)
    if dice == 6:
        break"""


#2
"""import  random


def x(y):
    return random.randint(1, y)


y = float(input("Give a number: "))

while True:
    z = x(y)
    print("The result of each roll is: ", z)
    if z == y:
        break"""


#3


"""def x(g):
    return 3.7854 * g

while True:
    z  = float(input("How many gallons to liters: "))
    if z < 0:
      print(" ")
      break
    if z >= 1:
     print(f"{z} gallon = {x(z):.1f} liters ")
    else:
        print(f"{z} gallon = {0} liter")"""


#6
"""import math


def pizza(d, p):
    return p/(math.pi * (d /2) ** 2)


p1 = float(input("1st pizza price: "))
d1 = float(input("1st pizza diameter: "))
p2 = float(input("2nd pizza price: "))
d2 = float(input("2nd pizza diameter:  "))

if pizza(p1, d1) < pizza(p2, d2):
    print("1st pizza is better.")
else:
    print("2nd pizza is better.")"""


#4


"""def sum(num):
    n1= 0
    for i in num:
        n1 += 1
    return n1



import random
num = []
for no in range(10):
    num.append(random.randint(1, 10))
print("The list: ")
for i in range(len(num)):
    print(num[i], end= " ")
print(f"\nSum of the list is {sum(num)}")"""


#5
"""def even(list_n):
    result_list = []
    for i in range(len(list_n)):
        if list_n[i] % 2 == 0:
            result_list.append(list_n[i])
    return result_list


def print_list(num, list_no):
    print(num, end=" ")
    for i in range(len(list_no)):
        print(list_no[i], end=" ")



import random
numberlist =[]
for n in range(10):
    numberlist.append(random.randint(1,99))
print_list("Here is the original number: ", numberlist)
cutdown_list =  even(numberlist)
print_list("\nCut down list is: ", cutdown_list)"""


#5(Alternate way)


"""def remove_odd_numbers(x):
    # using list comprehension to remove all odd numbers
    return [num for num in x if num % 2 == 0]


import random


def main():
    original_list = []
    for n in range(10):
        original_list.append(random.randint(1, 99))

    cutDown_list = remove_odd_numbers(original_list)

    print("Original List:", original_list)
    print("cutDown_list:", cutDown_list)


main()"""



"""def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

while True:
    user_input = int(input("Enter an integer (<= 0 to exit): "))
    if user_input <= 0:
       print("Exiting the program.")
       break
    else:
        result = factorial(user_input)
        print(f"The factorial of {user_input} is {result}")"""


"""def spruce(height):
    print("A spurce is coming!")
    i = 1


    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i += 1
    print(" " * (height - 1) + "*")


spruce(8)"""


"""def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


while True:
    num = int(input("Please type in an integer number: "))

    # Try to convert the user input to an integer
    # Check if the number is equal to or below 0
    if num <= 0:
        print("Execution ends.")
        break

    # Calculate and print the factorial
    print(f"The factorial of {num} is {factorial(num)}")"""


"""def sum_of_squares(first, second):
    result = first**2 + second**2
    return result

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = sum_of_squares(number1, number2)
print(f"The sum of squares for numbers {number1:.3f} and {number2:.3f} is {result:.3f}.")"""
import random

"""def inventory(x):
    print("You have the following items:")
    for item in x:
        print("- " + item)
    return

backpack = ["Water bottle", "Map", "Compass"]
inventory(backpack)
backpack.append("Swiss Army knife")
inventory(backpack)"""