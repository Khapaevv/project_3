import json


def load_operations():
    """вытаскиваем из json"""
    with open('../trash/operations.json', ) as f:
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


def get_date(i):
    """получаем дату"""
    date_0 = s[i]['date'].split("T")
    date = ".".join(date_0[0].split("-")[::-1])
    return date


def get_description(i):
    """получаем вид операции"""
    description = s[i].get('description')
    return description


def get_from_(i):
    """получаем от кого и заменяем звездочками"""
    from_ = s[i].get("from")
    from_stars = []
    if from_ == None:
        return
    else:
        if from_[-17:-16] == " ":
            from_stars = (from_[:-17] + " " + from_[-16:-12] + ' ' + from_[-13:-11] + '** **** ' + from_[-4:])
        else:
            from_stars = (from_[:4] + ' **' + from_[-4:])


    return from_stars
    # return from_stars
# get_from_(i)
# print(get_from_(3))

def get_to(i):
    """получаем кому и заменяем звездочками"""
    to = s[i].get("to")
    to_ = []
    if to[-17:-16] == " ":
        to_ = (to[:-17] + " " + to[-16:-12] + ' ' + to[-13:-11] + '** **** ' + to[-4:])
    else:
        to_ = (to[:4] + ' **' + to[-4:])
    return to_


def get_amount(i):
    """получаем сумму"""
    operationAmount = s[i].get('operationAmount')
    values = list(operationAmount.values())
    amount = values[0]
    return amount


def get_currency(i):
    """получаем название валюты"""
    operationAmount = s[i].get('operationAmount')
    values = list(operationAmount.values())
    currency = values[1]
    currency_values = list(currency.values())[0]
    return currency_values
