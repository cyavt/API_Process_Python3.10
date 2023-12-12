from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS  # Import the CORS module
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.icon', mimetypes='Desgin-E.png')
@app.route('/')
def index():
    return "Hello, Python!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from the backend Python! NVT'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)