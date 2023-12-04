from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/play', methods=['POST'])
def play_game():
    data = request.json
    player_choice = data.get('player')

    computer_choice = computer_turn()
    result = check_winner(player_choice, computer_choice)

    return jsonify({
        'player': player_choice,
        'computer': computer_choice,
        'result': result
    })

def computer_turn():
    rand_num = random.randint(1, 3)

    if rand_num == 1:
        return "ROCK"
    elif rand_num == 2:
        return "PAPER"
    else:
        return "SCISSORS"

def check_winner(player, computer):
    if player == computer:
        return "Draw!"
    elif computer == "ROCK":
        return "You Win!" if player == "PAPER" else "You Lose!"
    elif computer == "PAPER":
        return "You Win!" if player == "SCISSORS" else "You Lose!"
    elif computer == "SCISSORS":
        return "You Win!" if player == "ROCK" else "You Lose!"

if __name__ == '__main__':
    app.run(debug=True)
