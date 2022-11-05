from flask import Flask
import requests
app = Flask(__name__)
@app.route("/")
def get_parameters():
    print("123")
    return "<p>Hello, World!</p>"
    response = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2018%20Fall&department=COMPSCI&courseNumber=161")
    response.json()
