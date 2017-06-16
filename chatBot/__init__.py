from flask import Flask
from flask_cors import CORS, cross_origin

# App Instance
app = Flask(__name__)

# CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from . import chatBot
