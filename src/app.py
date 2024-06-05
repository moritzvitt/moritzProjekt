from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html', title='Language Reactor to Anki Converter')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file upload logic here
    file = request.files['fileUpload']
    # You can process the file and handle the selected configurations
    # For now, we'll just print the file name
    print(f"Uploaded file: {file.filename}")
    return "File uploaded successfully"
    

if __name__ == '__main__':
    print("Current working directory:", os.getcwd())
    app.run(debug=True)
# 
from flask import Flask, render_template
from flaskext.markdown import Markdown
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
Markdown(app)

@app.route('/')
def index():
    # Example Markdown content
    markdown_content = """
    # Welcome to My Flask App
    This is a simple example of combining **Markdown** with *Bootstrap*.
    
    ## Features
    - Easy to use
    - Simple integration
    - Powerful and flexible

    ```python
    # Sample code block
    def hello_world():
        print("Hello, world!")
    ```

    ![Example Image](static/images/francy.webp)
    """
    return render_template('index.html', title='Markdown with Bootstrap', content=markdown_content)

if __name__ == '__main__':
    print("Current working directory:", os.getcwd())
    app.run(debug=True)
