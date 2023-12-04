from flask import Flask, jsonify, request
import mysql.connector



app = Flask(__name__)

@app.route('/players', methods=['GET'])
def get_players():
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user="touhid",
        password="MyN3wP4ssw0rd",
        database="pingpong",
    )

    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM players')
    players = cursor.fetchall()
    return jsonify(players)

@app.route('/players', methods=['POST'])
def add_player():
    data = request.get_json()
    name = data['name']
    score = data['score']

    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user="touhid",
        password="MyN3wP4ssw0rd",
        database="pingpong",
    )

    cursor = connection.cursor(dictionary=True)
    cursor.execute('INSERT INTO players (name, score) VALUES (?, ?)', (name, score))

    return jsonify({'message': 'Player added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
