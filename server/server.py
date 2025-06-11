from flask import Flask, request, jsonify
import os
from pythonScripts import predict
from flask_cors import CORS
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)

# @app.route('/template')
# def index():
#     return render_template('index.html')

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

print("hello from back")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
        # return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    # print(file)
    if file.filename == '':
        return 'No selected file', 400
        # return jsonify({'message': 'No selected file'}), 400
    
    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        return "Failed to decode image", 400
    
    file_path = 'D:/buffer_/uploads/uploaded_image.jpg'
    cv2.imwrite(file_path, img)

    # if file:
    # file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    # print(file_path)
    # file.save(file_path)

    res = predict.giveResult(file_path)
    # print(type(res))
    # print(res)
    return res, 200, {'Content-Type': 'text/plain'}
    # return str(res), 200, {'Content-Type': 'text/plain'}
    # return jsonify({'prediction': res}), 200
    # Process the file (Example: Just returning the filename for now)
    # return jsonify({'message': f'File {file.filename} uploaded successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
