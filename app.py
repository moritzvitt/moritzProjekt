from flask import Flask, render_template, request, redirect, url_for, session
import os
import pandas as pd
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


# Set the folder to save uploaded files
UPLOAD_FOLDER = '/Users/moritzvitt/LR2Anki/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    df_html = session.get('df_html', None)
    return render_template('index.html', df_html=df_html)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'fileUpload' not in request.files:
        return redirect(request.url)
    file = request.files['fileUpload']
    if file.filename == '':
        return redirect(request.url)
    if file:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        native_language = request.form['nativeLanguage']
        
        json_file_path = '/Users/moritzvitt/LR2Anki/config/ger_config.json'

        # Open the JSON file and load its contents into a Python dictionary
        with open(json_file_path, 'r') as json_file:
            config_json = json.load(json_file)

        column_names = config_json['column_names']
        df = pd.read_csv(filepath, delimiter='\t', names=column_names)

        # native_language column
        df['native_language'] = native_language

        from orchestrator import main
        # processed_df = main(df, config_json)
        # # Convert DataFrame to HTML
        # df_html = processed_df.to_html(classes=["table", "table-striped"], border=0)
        # session['df_html'] = df_html  # Store the DataFrame HTML in session


        # # After processing, redirect to a new page or back to the form
        # return redirect(url_for('index'))

        processed_df = main(df, config_json)  # Assuming this returns a DataFrame
        df_html = processed_df.to_html(classes=["table", "table-striped"], border=0)
        session['df_html'] = df_html  # Update session with new HTML
        return redirect(url_for('index'))

# @app.route('/get-latest-values')
# def get_latest_values():
#     # This should return the latest values that need to be displayed on the table
#     # For demonstration, let's assume it returns a JSON object with a list of new values
#     new_values = ["Value 1", "Value 2"]  # Example new values
#     return jsonify(new_values)


if __name__ == '__main__':
    app.run(debug=True)
