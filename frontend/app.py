import os
from flask import Flask, render_template

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def home():
    backend_protocol = os.getenv('BACKEND_PROTOCOL', 'http')
    backend_host = os.getenv('BACKEND_HOST')
    backend_port = os.getenv('BACKEND_PORT')
    backend_url = f"{backend_protocol}://{backend_host}:{backend_port}"

    return render_template('index.html', backend_url=backend_url)
