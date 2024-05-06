from flask import Flask, render_template, request, redirect, url_for   
import os
import pandas as pd
import yaml

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


# Set the folder to save uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Home')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'fileUpload' not in request.files:
        return redirect(request.url)
    file = request.files.get('fileUpload')
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

    df = pd.read_csv(filepath, delimiter='\t')
    print(df.shape)

    native_language = request.form.get('languageSelect')
    print("native_language: ", native_language, "\n")
    
    # read the keys into a list 
    all_fields = []

    with open('config/messages.yaml', 'r') as file:
        messages = yaml.safe_load(file) 
        # Print all the keys
        for key in messages:
            all_fields.append(key)

    ticked_fields = request.form.getlist('tickedFields')
    print("wanted_fields: ", ticked_fields, "\n")

    # Create a dictionary where each key is a field name and each value is a boolean indicating whether the field is ticked
    wanted_fields = {field: field in ticked_fields for field in all_fields}
    print("wanted_fields: ", wanted_fields, "\n")

    # Wrap all the values wanted_fields and native_language in a config_dict
    config = {
        'wanted_fields': wanted_fields,
        'target_language': 'Japanese', # 'Japanese' is the default target language
        'native_language': native_language
    }
    
    print("config_dict: ", config, "\n")
    
    from orchestrator import main

    package, df = main(df, config)
    
    # # Return the selected fields, native language, and DataFrame as an HTML table
    return f'''
        These are your chosen preferences:
        <h2>Native Language: {native_language}</h2>
        <h2>Selected Fields: {wanted_fields}</h2>
        <h2>DataFrame:</h2>
        {df.head()}
    '''

if __name__ == '__main__':
    app.run(debug=True)

# %%
