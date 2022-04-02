from flask import Flask
from logger import trigger_log_save
from scrape import run as scrape_runner 

app = Flask(__name__)

# http://localhost:8000/
@app.route("/", methods=['GET'])
def hello_world():
    return "Hello world. This is flask"

# http://localhost:8000/again
@app.route("/again", methods=['GET'])
def hello_world_again():
    return "Hello world. This is flask (Again)"


@app.route("/box_office_mojo_scraper", methods=['POST'])
def box_office_scraper_view():
    trigger_log_save()
    scrape_runner()
    return {'Done': [1,2,3]}
