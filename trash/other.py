import json
from src.functions import get_from_



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

def sort_date():
    """сортируем по дате и выводим последние 5 операций"""
    sorted_data = sorted(executed_operations(), key=lambda x: x['date'], reverse=True)

    return sorted_data

# print(sort_5_last_date())
# def main():
#     """основной код"""
s = sort_date()
# print(s)

i = 5

def main():
    """нужно сделать скрытые счета, убать ноне из кому и все объеденить и потом тесты сделать"""
    for i in range(5):
        print(s[i])
        date_0 = []
        date_0 = s[i]['date'].split("T")
        # print(date_0)
        date = []
        # print(date_0[0].split("-"))
        date = ".".join(date_0[0].split("-")[::-1])
        print(date)
        description = []
        description = s[i].get('description')
        print(description)
        # from_stars = []
        from_ = s[3].get("from")
        print(from_)
        # print(from_[-4:])
        # print(from_[:4])
        # print(from_[4:6])
        # print(from_[-16:-12])
        # print(from_[-12:-10])
        # print(from_[-17:-16])
        # print(from_[:-17])
        if from_ == None:
           # from_stars = "gecnj"
           from_stars = "nothing"
        else:
           if from_[-17:-16] == " ":
               from_stars = (from_[:-17] + from_[-16:-12] + ' ' + from_[-12:-10] + '** **** ' + from_[-4:])
               from_stars = "kard"
           else:
               from_stars = (from_[:-21] + '**' + from_[-4:])
               from_stars = "schet"
        print(from_stars)
        # if from_ == None:
        #     from_stars = "gecnj"
        # else:
        #     if len(from_) == 16:
        #         from_stars.append(from_[:4] + ' ' + from_[4:6] + '** **** ' + from_[-4:])
        #     else:
        #         from_stars.append('**' + from_[-4:])
        #         from_stars = ' '.join(from_stars)
        #     return from_stars


        #
        # print(from_stars)
        # if get_from_(i) != None:
        # from_ = get_from_(i)
        # new_f = []
        # if from_ != None:
        #     new_f = from_[:-12] + "******" + from_[-6:]
        #     return new_f
        # else:
        #     continue

        # new_s = from_[:-10] +"******" + from_[:-5]
        # # from_1 = []
        # from_ = s[i].get("from")
        #
        # if from_ == None:
        #     continue
        # else:
        #     return from_
        # from_1 = list(from_)
        # print(from_)
        # print(new_f)
        # print(from_1)
        # print(new_s)
        to = s[i].get("to")
        to_ = []
        print(to)
        if len(to) == 16:
            to_.append(to[:4] + ' ' + to[4:6] + '** **** ' + to[-4:])
        else:
            to_.append('**' + to[-4:])
        to_ = ' '.join(to_)
        # new_s = to[-12:-6]
        # new_d = to[:-12]+"******"+to[-6:]
        # print(to)
        # print(new_s)
        # print(new_d)
        print(to_)
        operationAmount_a = []
        operationAmount = s[i].get('operationAmount')
        # operationAmount_a = operationAmount.split(",")
        values = list(operationAmount.values())
        amount = values[0]
        currency = values[1]
        currency_values = list(currency.values())[0]
        # operationAmount_c = s[i].get('operationAmount')[1]
        # print(operationAmount)
        # print(values)
        print(amount)
        # print(currency)
        print(currency_values)


        # print({date}{description}{from_}{to})
print(main())
    # print(date_0[0].strftime( % d - % m - %Y))
# date = []
# date = date_0.split("-")
# print(s[0]['date'].split("T"))
# print(date_0[0:1],date_0[1])
# print(sort_5_last_date()[4]['date'])
    # Пример вывода для одной операции:
    # 14.10 .2018
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




