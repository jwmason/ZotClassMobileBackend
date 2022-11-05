from flask import Flask
from flask import request
import requests
import json
app = Flask(__name__)
@app.route("/departments")

def all_departments():
    response1 = requests.get("https://api.peterportal.org/rest/v0/courses/all")
    resp_json = response1.json()
    set1 = set()
    for i in resp_json:
        x = i["department"]
        set1.add(x)
    dep_dict = {'json_list': list(set1)}
    json_data = json.dumps(dep_dict)
    return json_data

@app.route("/parameters")
# http://127.0.0.1:5000/parameters?term=2022Fall&department=ICS&sectionCodes=12345&courseTitle=31A

def get_parameters():
    term = request.args.get('term')
    department = request.args.get('department')
    section_code = request.args.get('sectionCodes')
    course_title = request.args.get('courseTitle')
    search_parameters = {'Term': term, 'Department': department, 'Section Code': section_code, 'Course Title': course_title}
    if term != "None":
        term_get = "term=" + str(term)
    else:
        term_get = ""
    if department != "None":
        department_get = "department=" + str(department)
    else:
        department_get = ""
    if section_code != "None":
        section_code_get = "sectionCodes=" + str(section_code)
    else:
        section_code_get = ""
    if course_title != "None":
        course_title_get = "courseTitle=" + str(course_title)
    else:
        course_title_get = ""
    string1 = term_get + " " + department_get + " " + section_code_get + " " + course_title_get
    string2 = string1.replace(" ", "&")
    print(string2)
    response2 = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?" + string2)
    return response2.json()
