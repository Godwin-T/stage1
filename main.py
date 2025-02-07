from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    length = len(digits)
    return sum(d ** length for d in digits) == n

def is_prime(n):
    """ Check if a number is a prime number. """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_number(n):
    """ Check if a number is a perfect number. """
    if n < 1:
        return False
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def is_odd_or_even(n):
    """ Determine if a number is odd or even. """
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def get_funfact(digit):

    url = f"http://numbersapi.com/{digit}/math"
    response = requests.get(url)
    fun_fact = response.text
    return fun_fact

def main(digit):


    armstrong = is_armstrong(digit)
    prime_no = is_prime(digit)
    perfect_no = is_perfect_number(digit)
    digit_sum = sum_of_digits(digit)
    digit_type = is_odd_or_even(digit)
    funfact = get_funfact(digit)

    response = {
            "number": digit,
            "is_prime": prime_no,
            "is_perfect": perfect_no,
            "properties": ["armstrong", digit_type] if armstrong else [digit_type],
            "digit_sum": digit_sum,
            "fun_fact": funfact
        }
    
    return response


@app.route('/')
def home():
    return jsonify({
        "message": "Number Analysis API", 
        "status": "running",
        "documentation": "/api/classify-number/?number=<integer>"
    })

@app.route('/api/classify-number/', methods=['GET'])
def number_info():
    try:
        number = request.args.get('number', default=None, type=int)
        response = main(number)
        print(response)
        return response
    except:
        return {
                            "number": "alphabet",
                            "error": True
                        }, 400

if __name__ == '__main__':
    app.run(debug=True)
