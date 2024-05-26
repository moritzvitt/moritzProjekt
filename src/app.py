from flask import Flask, render_template, request, redirect, url_for, session,  send_from_directory, send_file
import os
import pandas as pd
import yaml
from src.orchestrator import main
from deck import export_df

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


# Set the folder to save uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def index():
    df = pd.DataFrame(session.get('df', {}))  # Retrieve the DataFrame from the session
    return render_template('index.html', title='Home', df=df)

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
    with open('config/column_names.yaml', 'r') as file:
        data = yaml.safe_load(file)
        # the column names are stored in a list, the list's name is column_names
        column_names = data['column_names']
    

    # TODO target_langugage default value should come from df, show it to user directly when csv is uploaded

    # assign column_names to the dataframe
    df.columns = column_names
    # only select necessary columns like word
    dfa = df[['word', 'short_phrase', 'word_translation', 'long_phrase', 'machine_translation', 'human_translation']]
    session['dfa'] = dfa.to_dict()  # Convert the DataFrame to a dictionary and store it in the session
    session['df'] = df.to_dict()  # Convert the DataFrame to a dictionary and store it in the session

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

    config = {
        'wanted_fields': wanted_fields,
        'target_language': 'Japanese', # 'Japanese' is the default target language
        'native_language': native_language
    }

    # store config in the session
    session['config'] = config
    
    return render_template('upload.html', title='upload', native_language=native_language, wanted_fields=ticked_fields, df=dfa)


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    # Call the main function from orchestrator.py

    DOWNLOAD_FOLDER = 'downloads'
    app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER 
    # Retrieve the DataFrame, config, and package from the session
    df = pd.DataFrame(session.get('df', {}))
    config = session.get('config', {})
    package, df = main(df, config)
    # write the file path to the Downloads folder into a variable
    
    # only take important field like synonyms from df
    df = df[['word', 'short_phrase', 'word_translation', 'long_phrase', 'machine_translation', 'human_translation', 'synonyms', 'test', 'explanation']]
    output_file_path = os.path.join(app.config['DOWNLOAD_FOLDER'])
    package_path, csv_file_path = export_df(df, package, config, output_file_path)
    # write the paths to the session
    session['package_path'] = package_path
    session['csv_file_path'] = csv_file_path
    
    return render_template('generate.html', title='Home', df=df, package_filename=package_path, csv_path=csv_file_path)


@app.route('/download/<file_type>', methods=['GET'])
def download(file_type):
    if file_type == 'package':
        file_path = session.get('package_path', None)
    elif file_type == 'csv':
        file_path = session.get('csv_file_path', None)
    else:
        return "Invalid file type requested", 400

    if file_path is None:
        return "File not found", 404

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

# %%
