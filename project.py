import random

print("Instruction: To unlock the level 2 either you have to get 6 by rolling the dice or you have to answer 6 questions correctly.")

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
#num_of_dice = int(input("How many dice?: "))
num_of_dice = 1

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# PRINT VERTICALLY
#for die in range(num_of_dice):
    #for line in dice_art.get(dice[die]):
       #print(line)

# PRINT HORIZONTALLY
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    print(f"total: {die}")
    if die == 6:
        print("Congratulation! You've unlocked the level 2.")
    else:
        questions = ("How many elements are in the periodic table?: ",
                     "Which animal lays the largest eggs?: ",
                     "What does Newton's first law of motion cover?: ",
                     "How many bones are in the human body?: ",
                     "What is the value of square root 25?: ",
                     "Which planet in the solar system is the hottest?: ")

        options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Gravity", "B. Energy", "C. Inertia", "D. Density"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. 5", "B. 6", "C. 2", "D. 3"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

        answers = ("C", "D", "C", "A", "A", "B")
        guesses = []
        score = 0
        question_num = 0

        for question in questions:
            print("----------------------")
            print(question)
            for option in options[question_num]:
                print(option)

            guess = input("Enter (A, B, C, D): ").upper()
            guesses.append(guess)
            if guess == answers[question_num]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"{answers[question_num]} is the correct answer.")
            question_num += 1
        print("                      ")
        print("       RESULTS        ")
        print("                      ")

        print("answers: ", end="")
        for answer in answers:
            print(answer, end=" ")
        print()

        print("guesses: ", end="")
        for guess in guesses:
            print(guess, end=" ")
        print()

        score = int(score)

        if score == 6:
            print(f"Your score is: {score}p")
            print("Congratulations! You've unlocked level 2")
        else:
            print(f"Your score is {score}p")
            print("You can't unlock the level 2 until you answer 6 questions correctly.")
            print("Try again!")


print("----------------------")
print("                      ")
print("       LEVEL 2        ")
print("                      ")
print("----------------------")


if die ==  6 or score == 6:
    print("To win the game you need to reach the End position")
    print("X represents walls and  S represents Start. The player(You) is represented by P and can move by typing w (up), a (left), s (down), or d (right).")

    import sys

    # Maze layout
    maze = [
        ["S", " ", " ", " ", " ", "X", " ", " ", " ", "End"],
        ["X", "X", " ", "X", "X", "X", " ", "X", " ", "X"],
        [" ", " ", " ", " ", " ", " ", " ", "X", " ", " "],
        [" ", "X", "X", "X", " ", "X", "X", "X", " ", "X"],
        [" ", " ", " ", "X", " ", " ", " ", " ", " ", " "],
        [" ", "X", " ", " ", " ", "X", " ", "X", " ", "X"],
        [" ", " ", " ", "X", " ", "X", " ", " ", " ", " "],
        [" ", "X", " ", "X", " ", "X", " ", "X", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", "X", " ", "X", " ", "X", " ", "X", " ", " "]
    ]

    # Player position
    player_pos = [0, 0]


    def print_maze():
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if [row, col] == player_pos:
                    print("P", end=" ")

                else:
                    print(maze[row][col], end=" ")
            print()


    def move_player(direction):
        if direction == "w":  # Up
            if player_pos[0] > 0 and maze[player_pos[0] - 1][player_pos[1]] != "X":
                player_pos[0] -= 1
        elif direction == "s":  # Down
            if player_pos[0] < len(maze) - 1 and maze[player_pos[0] + 1][player_pos[1]] != "X":
                player_pos[0] += 1
        elif direction == "a":  # Left
            if player_pos[1] > 0 and maze[player_pos[0]][player_pos[1] - 1] != "X":
                player_pos[1] -= 1
        elif direction == "d":  # Right
            if player_pos[1] < len(maze[0]) - 1 and maze[player_pos[0]][player_pos[1] + 1] != "X":
                player_pos[1] += 1


    def is_win():
        return maze[player_pos[0]][player_pos[1]] == "End"


    # Game loop
    while True:
        print_maze()

        if is_win():
            print("                      ")
            print("                      ")
            print("       YOU WON        ")
            print("                      ")
            print("                      ")
            sys.exit()

        move = input("Move (w/a/s/d): ")
        move_player(move)



