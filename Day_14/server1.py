from flask import Flask

app = Flask(__name__)

# http://localhost:8000/
@app.route("/", methods=['GET'])
def hello_world():
    return "Hello world. This is flask"

# http://localhost:8000/again
@app.route("/again", methods=['GET'])
def hello_world_again():
    return "Hello world. This is flask (Again)"