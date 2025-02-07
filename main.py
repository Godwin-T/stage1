from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def is_armstrong(n):
    if n < 0:
        return False  # Armstrong numbers are non-negative
    digits = [int(d) for d in str(n)]  # Work with the absolute value of n, convert n to int to drop decimal part
    length = len(digits)
    return sum(d ** length for d in digits) == n

def is_prime(n):
    """ Check if a number is a prime number. """
    n = abs(int(n))  # Consider absolute value for primality test, convert to int to handle floats
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_number(n):
    """ Check if a number is a perfect number. """
    n = abs(int(n))  # Only positive integers can be perfect numbers, handle floats by converting to int
    if n < 1:
        return False
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def sum_of_digits(n):
    absolute_value = abs(n)
    return sum(int(digit) for digit in str(absolute_value))  # Handle floats by taking absolute and converting to string

def is_odd_or_even(n):
    """ Determine if a number is odd or even. """
    n = int(n)  # Convert n to integer to perform modulus operation
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

def get_funfact(digit):
    url = f"http://numbersapi.com/{int(digit)}/math"  # Ensure digit is integer for API call
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
        "documentation": "/api/classify-number/?number=<number>"
    })

@app.route('/api/classify-number/', methods=['GET'])
def number_info():
    number = request.args.get('number', type=float)  # Accept float values directly
   
    try:
        response = main(int(number))
        return jsonify(response), 200
    except:
           return {
        "number": "alphabet",
        "error": True
    }, 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000, debug=True)
