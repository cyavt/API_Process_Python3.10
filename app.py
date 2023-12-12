from flask import Flask, jsonify
from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from the backend Python! NVT'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)