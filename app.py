# 1. Write a Google app engine program to generate n even number
# and deploy it to Google cloud

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generate_even_numbers():
    # total even numbers to generate
    n = 10
    if n < 0:
        return jsonify({'error': 'Invalid input. Please provide a non-negative integer.'}), 400
    
    even_numbers = [i for i in range(2, (n * 2) + 1, 2)]
    
    return jsonify({'even_numbers': even_numbers})

if __name__ == '__main__':
    app.run()
