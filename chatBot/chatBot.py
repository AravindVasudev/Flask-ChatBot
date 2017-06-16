from flask import request
from flask_cors import cross_origin
from . import app
from .model import interpreter
from .answers import answers

@app.route('/')
def index():
    # get the `q` query parameter
    question = request.args.get('q')
    if question:
        response = interpreter.parse(question) # pass the question to the model to get response dictionary
        key = response['intent']['name'] # get the intent name from the dictionary
        return answers.get(key, 'oops! I don\'t understand ;(') # get the appropriate answer for the intent from the Key-Value pair and return
    else:
        return 'oops!'
