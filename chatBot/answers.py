'''
This file reads ../data/answers.json into answers as dictionary.
'''

import json

answers = []
with open('./data/answers.json') as json_data:
    answers = json.load(json_data)
