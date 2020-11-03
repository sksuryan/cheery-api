from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, request
from db import returnRandomMessage, addUserMessage

app = Flask(__name__)

@app.route('/')
def default():
    return jsonify("Cheery API built by @sksuryan")

@app.route('/get',methods=['GET'])
def getRandomQuote():
    return jsonify({'message': returnRandomMessage()}), 200

@app.route('/post',methods=['POST'])
def postQuote():
    message = request.json['message']
    addUserMessage(message)

    return jsonify({'message': 'ok'}), 200

if __name__ == '__main__':
    app.run()