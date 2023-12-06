"""
create a virtual environment:
    python3 -m venv .venv

On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command (you may need to use sudo).
    apt install python3.10-venv
Now create the virtual environment:
    python3 -m venv .venv

Activate the virtual environment
    source .venv/bin/activate

Install flask
    pip install flask

Run the app
     python3 flask_app.py

You can now open the page in your browser:
    localhost:5000/greeting

Or you can use a command line tool like curl:
    curl localhost:5000/greeting
    Output:
    Hello World
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return 'Root Page\n'

@app.route('/greeting', methods=['GET'])
def hello():
    return 'Hello World!\n'

@app.route('/json', methods=['GET'])
def json():
    return jsonify({'name': "noe", "age": 28})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
