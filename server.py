from flask import Flask, send_from_directory
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def serve_html():
    return send_from_directory(BASE_DIR, 'index.html', mimetype='text/html')

@app.route('/api/hello')
def api_hello():
    return {'message': 'Ciao dal server Python su Render!'}
