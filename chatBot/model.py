'''
This file loads the model and creates the interpreter object.
'''

from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.config import RasaNLUConfig

# Load the trained model as an object
metadata = Metadata.load('./models/trained')
interpreter = Interpreter.load(metadata, RasaNLUConfig('config.json'))
