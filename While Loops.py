

#1
"""x = 1
while x <=  1000:
    if x %  3 ==  0:
        print(x)
    x += 1"""

#2
"""while True:
    x =  float(input("Enter inches: "))
    if x < 0:
        print("The program ends.")
        x += 1
        break
    else:
        y = x * 2.54

        print(y)"""


#5
"""x = "python"
y = "rules"
attempts = 2
attempt = 0
while attempt < attempts:
    username = input("Enter your username: ")
    password = input("Enter your password:")
    if username == x and password ==  y:
        print("Welcome")
    else:
        print("Try again")
        attempt += 1
if attempt == attempts:
    print("Access denied")"""
"""i  = 0
while i< 3 :
    print("HI")
    i += 1"""

"""import random
dice1 = dice2 = rolls = 0
while (dice1!=6 or dice2!=6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1
print(f"Rolled {rolls:d} times.")"""
"""command = input("Enter command: ")
while command!="":
    if command=="MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
print("Execution stopped.")"""

"""command = input("Enter command: ")
while command!="stop":
    if command=="MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
else:
    print("Goodbye.")
print("Execution stopped.")"""
# Faulty program, infinite loop

"""number = 1
while number<5:
    print(number)
    number += 1

# This part is never reached:
print("All ready.")"""

"""while True:
    # Get user input for inches
    inches = float(input("Enter a length in inches (or a negative value to exit): "))

    # Check if the user wants to exit
    if inches < 0:
        print("Exiting the program.")
        break

    # Convert inches to centimeters
    centimeters = inches * 2.54
    # Display the result
    print(f"{inches} inches is equal to {centimeters} centimeters")"""""
# Faulty program, infinite loop

#4
"""import random
secret_number = random.randint(1,6)
guess  = int(input("Guess the number: "))
while guess != secret_number:
    if guess >  secret_number:
        print("Too high")
    #elif guess < secret_number:
        #print("Too low")
    else:
        print("Too low ")
    guess = int(input("Guess the number: "))

print("correct")"""

#5
"""username = "python"
password = "rules12"
re_try = 0
while re_try < 5:
    u = input("Give the username?: ")
    p = input("Give the password?: ")
    if u == username and p == password:
        print ("Welcome")
        break
    re_try += 1
else:
    print("Access denied")"""
#2
"""while True:
    x = int(input("Enter the number: "))
    if x < 0:
        print("Ends")
        break

    y = x * 2.54
    print (y)"""
#3
"""largest = None
smallest = None
while True:
    s = input("number: ")
    if s == "":
        print("no number")
        break
    if largest is None or int(s) > largest:
        largest = int(s)
    if smallest is None or int(s) < smallest:
        smallest = int(s)
    print(smallest, largest)"""""
"""pin = 1234
x = input("Do you want to pay (yes/no): ")
if x == "yes":
    z =  int(input("Enter your pin"))
    if z == pin:
        print("Paid")
    else:
        n = 0
        while n < 2:
            print("Incorrect PIN. Please try again.")
            z = int(input("Please re-enter your PIN code: "))
            n += 1
    if n == 2:
        print("Payment canceled")
elif x != "yes":
    print("Access  denied")"""

#6

"""import random
N = int(input("How many random points to generate?: "))
n = 0
i = 0
while  i < N :
    x = random.uniform(-1.0,1.0)
    y = random.uniform(-1.0,1.0)

    if x**2 + y**2 < 1.0:
        n += 1

    i += 1

import math

pi = 4.0 * n/N
print(f"Pi is {pi}, error {math.pi - pi}")"""


"""i = int(input("How many greeting: "))
z = 1
while z <= i:
    print("Good\nmorning")
    z = z + 1"""
import math

"""x = input("Enter command: ")
while x !="stop":
    print("", x)
    x = input("Enter command: ")"""


"""import random
dice1 = dice2 = rolls = 0
while (dice1 != 6 or dice2 !=6):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1,6)
    rolls += 1
print(f"Rolled {rolls:d} times. ")"""

"""import random
rounds = 0
total_rolls = 0
while  rounds < 100000:
    dice1 = dice2 = rolls = 0
    while (dice1 != 6 or dice2 != 6):
        dice1= random.randint(1,6)
        dice2= random.randint(1,6)
        rolls += 1

    rounds += 1
    total_rolls = total_rolls +  rolls
average_rolls = total_rolls/rounds
print (f"Average rolls required: {average_rolls:.4f}")"""

"""x = int(input("Enter your number: "))
while x <= 10:
    y = 1
    while y  <=  10:
        print(f"{x} times {y} is {x*y:d}")
        y += 1
    x += 1"""
"""pay = input("How would you like to pay? Yes/No: ")

if pay == "yes":
    print("Please present your bank card")
    correct_pin = 1234  # Use the actual correct PIN here

    input_pin = int(input("Please enter your PIN code: "))

    if input_pin == correct_pin:
        print("PIN verified. Payment successful.")
    else:
        reattempt = 0
        while reattempt < 3:
            print("Incorrect PIN. Please try again.")
            input_pin = int(input("Please re-enter your PIN code: "))
            reattempt += 1

        if reattempt == 3:
            print("Maximum PIN attempts reached. Payment rejected.")
elif pay == "no":
    print("Payment cancelled")"""

"""import random
x = random.randint(1, 100)
attempts = 0
print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100. Try to guess it.")

while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < x:
            print("Too low! Try again.")
        elif user_guess > x:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {x} in {attempts} attempts.")"""
"""x = int(input("Type an integer number: "))
if x <= 0:
    print("The  execution ends")
factorial = 1
new = 1
while new <= x:
    factorial = factorial * new
    new += 1
    print(f"The factorial of the number {x} is {factorial}")"""









