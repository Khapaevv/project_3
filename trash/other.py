import json


def load_operations():
    with open('operations.json', ) as f:
        return json.load(f)

# print(load_operations())
list_executed = []
def executed_operations():
    for i in load_operations():
        print(i)
        if i["state"] == "EXECUTED":
            list_executed.append(i)
            print(list_executed)
        # load_operations()

            # list_executed.append(i)
            # return list_executed
#
print(executed_operations())


# print(load_operations()[state])

# def get_student_by_pk(pk):
#     ls = load_students()
#     for student in ls:
#         if student["pk"] == pk:
#             return student




