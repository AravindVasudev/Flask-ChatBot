from flask import Flask
from flask_cors import CORS, cross_origin

# App Instance
app = Flask(__name__)

# CORS
CORS(app)

from . import chatBot
