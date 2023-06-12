from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generate_even_numbers():
    n = 10
    if n < 0:
        return jsonify({'error': 'Invalid input. Please provide a non-negative integer.'}), 400
    
    even_numbers = [i for i in range(2, (n * 2) + 1, 2)]
    
    return jsonify({'even_numbers': even_numbers})


# def hello_world():
#     return 'Hello, World!'

if __name__ == '__main__':
    app.run()
