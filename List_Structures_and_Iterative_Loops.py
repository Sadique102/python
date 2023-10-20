"""names = []

name = input("Enter your name or quit by enter: ")
while name !="":
    names.append(name)
    name = input("Enter your name or quit by enter: ")
for n in names:
    print(f"Hello {n}!")"""

#1
"""x = int(input("How many dice to roll?: "))
_sum =  0
import random
for _ in range(x):
    rolls = random.randint(1,6)
    print(rolls)
    _sum += rolls

print(f"The sum of the  numbers:", _sum)"""

#2

"""numbers = []
while True:
    x = input("Enter a number or press Enter button: ")
    if x == "":
        print("")
        break

    y = float(x)
    numbers.append(y)

if len(numbers) >= 5:
    numbers.sort(reverse=True)
    print("The five greatest numbers sorted in descending order:  ")
    for i in range(5):
        print(numbers[i])
else:
    print("You entered fewer than five numbers ")"""

#3
"""num = int(input("Give a number:"))

if num > 1:
    for n in range(2, num):
        if num % n == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")#Negative integers can not be prime."""


#4

"""cities = []

for i in range(5):
    city_name = input(f"Enter the name of city {i + 1}: ")
    cities.append(city_name)

print("City names entered by the user:")
for city in cities:
    print(city)"""






