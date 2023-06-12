# 4. nth largest number from a given list

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def nth_largest():
    # nth number
    n = 3
    # given list
    number_list = [12, 18, -1, 0, 7, 97, 23]
    sorted_num_list = sorted(number_list, reverse=True)
    return jsonify({
        'Number list': str(number_list),
        f'{n}th largest number': sorted_num_list[n-1]
        })

if __name__ == '__main__':
    app.run()
