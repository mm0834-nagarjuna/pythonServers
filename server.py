import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from DataBaseConnection import dbConnect
from GeminiLLMmodel import model
from generateSQL import generateSQL
from executeSql import execute_query

application = Flask(__name__)
CORS(application)
port = int(os.environ.get('PORT', 8080))

@application.route('/')
def newtest():
    return jsonify({"message": "Hello, World!"})

@application.route('/test', methods=['GET'])
def myfunction():
    data = [
        {'Name': 'Deba', 'Id': 1, 'Role': 'Developer', 'Location': 'Kolkata'},
        {'Name': 'Kunal', 'Id': 2, 'Role': 'Support', 'Location': 'Bengalore'},
        {'Name': 'Shila', 'Id': 3, 'Role': 'Developer', 'Location': 'Hyderabad'},
        {'Name': 'Asish', 'Id': 4, 'Role': 'Tester', 'Location': 'Bhubaneswar'},
        {'Name': 'Umesh', 'Id': 5, 'Role': 'Architect', 'Location': 'Pune'},
        {'Name': 'Raja', 'Id': 6, 'Role': 'Support', 'Location': 'Hyderabad'}
    ]
    return jsonify(data)

@application.route('/generate', methods=['POST'])
def  generate():
    data = request.json
    question = data.get('question')  
    sql =  generateSQL(model, question) 
    if sql == []:
        return jsonify({"prompt": question, "updateError":"Something went wrong..."})
    else :
            resData = execute_query(sql)
            if 'error' in resData:
                return jsonify({'error': resData['error'], "prompt": question, "message":resData['message']}), 400
            else:
                return jsonify({'data': resData.get('data'), "prompt": question, "query":resData.get('query')})

    
if __name__ == '__main__':
    application.debug = True
    application.run(host='0.0.0.0', port=port)
