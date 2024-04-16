import os
from flask import Flask, jsonify
from routes.books_api import get_blueprint
from db_helper import DBHelper
import dotenv
from flask_cors import CORS


dotenv.load_dotenv() # Load the environment variable from .env file

DBHelper.configure_mongo() # Configure the DBHelper

app = Flask(__name__) #__name__ is the name of the current file i.e. it will start with the current file
CORS(app)




# MiddleWares
# Executes before each and every request
@app.before_request #here the @ is an deprecator like in spring we uesd @ for annotation and before_request is predefined we cant change that
def before():
    print("Hii I am from before_request ")



#Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message':'404 Not Found'}), 404

# @app.route('/api/hello', methods=['GET']) #To define the route
# def get_hello():
#     return jsonify({'message':'Hello world!'})


# @app.route('/api/hello/<name>', methods=['GET'])
# def get_hello_name(name):
#     return jsonify({'message' : f'Hello {name}!'}) #here we have not mentioned the status of request which is 200 or we can use  make response function
#                                                    # return make_response(jsonify({'Message} : f'Hello {name}!'),200)



#Configuring the bluePrint
app.register_blueprint(get_blueprint())



port = os.getenv('FLASK_PORT','5000')


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port = port)