#!/usr/bin/env python3

from flask import Flask
import sys

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string>')
def print_string(string):
    print(string)  # Prints the string to the console
    return string

# Count route
@app.route('/count/<int:num>')
def count(num):
    result = '\n'.join(str(i) for i in range(num))  # Counting from 0 to 'num - 1'
    return result + '\n'  # Add a newline after the last number



# Math operation route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Division by zero is not allowed.", 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return f"Error: Unsupported operation '{operation}'.", 400

    return str(result)  # Return the result as a plain string, not wrapped in <h1>

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5555)
