import time
from flask import Flask
from flask_cors import CORS, cross_origin
import socket

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
@cross_origin()
def hello():
    return 'Hello World! from the backend host: {}.\n'.format(socket.gethostname())


@app.route('/time')
@cross_origin()
def get_current_time():
    return {
        'time': time.time()
    }
