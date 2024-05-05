from flask import Flask, render_template, request, redirect, url_for, session
import os
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


# Set the folder to save uploaded files
UPLOAD_FOLDER = '/Users/moritzvitt/LR2Anki/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Home')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'fileUpload' not in request.files:
        return redirect(request.url)
    file = request.files('fileUpload')
    if file.filename == '':
        
        return redirect(request.url)
    if file:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        native_language = request.form.get['languageSelect']
    
    

if __name__ == '__main__':
    app.run(debug=True)
