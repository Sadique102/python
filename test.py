
import random


def roll_die(faces):
 return random.randint(1, faces)


def roll_(num_dice, faces):

 total = 0
 for _ in range(num_dice):
     total += roll_die(faces)
 return total


def main():

    x = input("Enter your name:")
    print(x)
    num_dice = int(input("Enter the number of dice: "))
    faces = int(input("Enter the number of faces on a die: "))
    total = roll_(num_dice, faces)
    print(f"There are {num_dice} dice with {faces} faces. The dice total is {total}.")

main()
