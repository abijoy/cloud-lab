# 2. Google app engine program multiply two matrices

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def matrix_multiply():
    # the matrices
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]

    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Invalid input. Matrices are not compatible for multiplication.")

    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return str(result)

if __name__ == '__main__':
    app.run()
