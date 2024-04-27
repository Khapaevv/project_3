import json


def load_operations():
    """вытаскиваем из json"""
    with open('operations.json', ) as f:
        return json.load(f)

list_operation = []
list_operation_exe = []

def executed_operations():
    """выбираем только "EXECUTED" и складывем в отдельный список"""
    for operation in load_operations():
        if operation.get("state") == "EXECUTED":
            list_operation_exe.append(operation)

    return list_operation_exe

def sort_5_last_date():
    """сортируем по дате и выводим последние 5 операций"""
    sorted_data = sorted(executed_operations(), key=lambda x: x['date'], reverse=True)

    return sorted_data[:5]

print(sort_5_last_date())
# def main():
#     """основной код"""
s = sort_5_last_date()
date_0 = []
date_0 = s[0]['date'].split("T")
date = []
# date = date_0.split("-")
print(s[0]['date'].split("T"))
print(date_0[0:1],date_0[1])
print(sort_5_last_date()[4]['date'])
    # Пример вывода для одной операции:
    # 14.10
    # .2018
    # Перевод
    # организации
    # Visa
    # Platinum
    # 7000
    # 79 ** ** ** 6361 -> Счет ** 9638
    # 82771.72
    # руб.
#
#     for date in executed_operations():
#         print(date)
# def count_executed_operations():
#     index_lst_oper = 0
#     index_lst_oper = len(list_operation.exe) - 1


# # print(list_operation[index_lst_oper]["state"])
#
# sort_date()
    # from datetime import datetime
#
#     timestamps = ["2020-01-02 04:05:06", "2020-01-03 07:08:09", "2020-01-01 01:02:03"]
#     # Преобразуем в объекты datetime
#     datetime_objects = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in timestamps]
#     # Сортируем список объектов datetime по убыванию
#     datetime_objects.sort(reverse=True)


# list_operation.append(operation)
# index_lst_oper = 0
# index_lst_oper = len(list_operation) - 1
# # print(list_operation[index_lst_oper]["state"])
# if list_operation[index_lst_oper]["state"] == "EXECUTED":
#     list_operation_exe.append(list_operation[index_lst_oper])


# # print(list_operation[0])
# return list_operation_exe
#     print(index_lst_oper)
#     return list_operation[index_lst_oper]["state"] = 0
    # print(list_operation[10]["state"])
    # print(list_operation[index_lst_oper]["state"])
        #     list_operation_exe.append(list_operation[index_lst_oper])
    # print(len(list_operation_exe))
    # print(index_lst_oper)

        # if list_operation[index_lst_oper]["state"] == "EXECUTED":
        #     list_operation_exe.append(list_operation[index_lst_oper]["state"])
        # print(list_operation_exe)

    # print(index_lst_oper)
    # print(list_operation[index_lst_oper])
    # print(list_operation[index_lst_oper]["state"])
        # list_operation_exe.append([list_operation(len(list_operation)-1)]["state"] == "EXECUTED")
        # return list_operation_exe
        # print(len(list_operation_exe))
        # print(list_operation_exe)



#
# def sort_by_date():
#     for date in executed_operations():



        # print(list_operation[len(list_operation)-1]["state"] == "EXECUTED")
        # print(operation)
        # if operation["state"] == "EXECUTED":
        #     list_operation.append(operation)
        #     print(list_operation)
        # load_operations()

            # list_executed.append(i)
            # return list_executed
#



# print(load_operations()[state])

# def get_student_by_pk(pk):
#     ls = load_students()
#     for student in ls:
#         if student["pk"] == pk:
#             return student




