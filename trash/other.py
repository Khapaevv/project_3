import json


def load_operations():
    with open('operations.json', ) as f:
        return json.load(f)


def get_student_by_pk(pk):
    ls = load_students()
    for student in ls:
        if student["pk"] == pk:
            return student


import json

file = open("example.json")
json.load(file)