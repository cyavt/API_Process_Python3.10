from process import run_img_to_text, run_autoclick, run_remove_bg

from flask import Flask, jsonify, send_from_directory, request, render_template
from flask_cors import CORS  # Import the CORS module
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = 'text.png'
            file_path = os.path.join('uploads', filename)
            uploaded_file.save(file_path)
            print(file_path)
            result = run_img_to_text(file_path)

    return render_template('index.html', result=result)


def process_input(user_input):
    return user_input


@app.route('/api/img_to_text', methods=['GET', 'POST'])
def img_to_text():
    data = {
        "code": 200,
        "message": "Vui long nhap du lieu"
    }
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = 'text.png'
            file_path = os.path.join('uploads', filename)
            uploaded_file.save(file_path)
            message = run_img_to_text(file_path)
            data = {
                "code": 200,
                "message": message
            }
    return jsonify(data)


@app.route('/api/remove_bg', methods=['GET', 'POST'])
def remove_bg():
    data = {
        "code": 200,
        "message": "Vui long nhap du lieu"
    }
    if request.method == 'POST':
        uploaded_file = request.files['img']
        if uploaded_file.filename != '':
            filename = 'removebg.png'
            file_path = os.path.join('uploads', filename)
            # full_path = os.path.join(app.root_path, file_path)
            uploaded_file.save(file_path)
            run_remove_bg(file_path)
            data = {
                "code": 200,
                "url_img": request.url_root + file_path
            }
    return jsonify(data)

@app.route('/uploads/<path:filename>', methods=['GET'])
def download(filename):
    full_path = os.path.join(app.root_path, 'uploads')
    return send_from_directory(full_path, filename)

@app.route('/api/autoclick', methods=['GET', 'POST'])
def autoclick():
    data = {
        "code": 200,
        "message": "Vui long nhap du lieu RUN"
    }
    if (request.method == 'POST'):
        if request.form['state'] != '' and request.form['state'] == 'run':
            username = request.form['username']
            password = request.form['password']
            result = run_autoclick(username, password)
            data = {
                "code": 200,
                "message": result
            }
    return jsonify(data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    # app.run(port=int(os.environ.get("PORT", 7000)))
    app.run(debug=True)