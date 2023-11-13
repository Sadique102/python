from flask import Flask, request, jsonify

app = Flask(__name__)
""""@app.route('/sum')
def calculate_sum():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    total_sum = number1+number2
    return str(total_sum)

@app.route('/s')
def calculate_s():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    total_s = number1*number2
    return str(total_s)"""


"""def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>')
def check_prime(number):
    result = {"Number": number, "isPrime": is_prime(number)}
    return jsonify(result)"""

airport_database = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},

}

@app.route('/airport/<icao>')
def get_airport_info(icao):
    airport_info = airport_database.get(icao.upper())
    if airport_info:
        result = {"ICAO": icao.upper(), "Name": airport_info["Name"], "Location": airport_info["Location"]}
        return jsonify(result)
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
