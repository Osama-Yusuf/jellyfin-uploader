from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
DOWNLOADS_PATH = './downloads'  # Adjust if necessary

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/list-directories', methods=['GET'])
def list_directories():
    directories = [d for d in os.listdir(DOWNLOADS_PATH)
                   if os.path.isdir(os.path.join(DOWNLOADS_PATH, d))]
    return jsonify(directories)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        directory = request.form.get('directory')
        filepath = os.path.join(DOWNLOADS_PATH, directory, file.filename)
        file.save(filepath)
        return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)