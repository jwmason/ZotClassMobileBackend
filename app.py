from flask import Flask
from flask import request
import requests
import json
app = Flask(__name__)
@app.route("/")

def all_departments():
    response1 = requests.get("https://api.peterportal.org/rest/v0/courses/all")
    resp_json = response1.json()
    set1 = set()
    for i in resp_json:
        x = i["department"]
        set1.add(x)
    print(set1)
    return "hello"

'''def get_parameters():
    # user_parameters = input()
    term = request.args.get('term')
    department = request.args.get('department')
    section_code = request.args.get('section_code')
    course_title = request.args.get('course_title')
    search_parameters = {'Term': term, 'Department': department, 'Section Code': section_code, 'Course Title': course_title}
    if term == "None":
        term_get = ""
    if department == "None":
        department_get = ""
    if section_code == "None":
        section_code_get = ""
    if course_title == "None":
        course_title_get = ""
    response = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2018%20Fall&department=COMPSCI&courseNumber=161")
    return response.json()'''
