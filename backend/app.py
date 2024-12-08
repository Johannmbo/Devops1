from flask import Flask, request, jsonify
from flask_cors import CORS
#import json

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json.get('data')
    with open('data.txt', 'w') as f:
        f.write(data)
    return {'message': 'Data received '}


@app.route('/fetch', methods=['GET'])
def fetch():
    with open('data.txt', 'r') as f:
        data = f.read()
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(port=5000)