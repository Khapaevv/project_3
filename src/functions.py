import json


def load_operations():
    """открываем json"""
    with open('operations.json', encoding="utf-8") as f:
        return json.load(f)


def executed_operations(operations):
    """выбираем только "EXECUTED" и складывем в отдельный список"""
    list_operation_exe = []
    for operation in operations:
        if operation.get("state") == "EXECUTED":
            list_operation_exe.append(operation)

    return list_operation_exe


def sort_date(operations):
    """сортируем по дате"""
    sorted_data = sorted(operations, key=lambda x: x['date'], reverse=True)

    return sorted_data


def get_date(operation):
    """получаем дату"""
    date_0 = operation['date'].split("T")
    date = ".".join(date_0[0].split("-")[::-1])
    return date


def get_description(operation):
    """получаем вид операции"""
    description = operation.get('description')
    return description


def get_from_(operation):
    """получаем от кого и заменяем звездочками"""
    from_ = operation.get("from")
    if from_ == None:
        return
    else:
        if from_[-17:-16] == " ":
            from_stars = (from_[:-17] + " " + from_[-16:-12] + ' ' + from_[-12:-10] + '** **** ' + from_[-4:])
        else:
            from_stars = (from_[:4] + ' **' + from_[-4:])

    return from_stars


def get_to(operation):
    """получаем кому и заменяем звездочками"""
    to = operation.get("to")
    if to[-17:-16] == " ":
        to_ = (to[:-17] + " " + to[-16:-12] + ' ' + to[-12:-10] + '** **** ' + to[-4:])
    else:
        to_ = (to[:4] + ' **' + to[-4:])
    return to_


def get_amount(operation):
    """получаем сумму"""
    return operation['operationAmount']['amount']
    # operation_amount = operation.get('operationAmount')
    # values = list(operation_amount.values())
    # amount = values[0]
    # return amount


def get_currency(operation):
    """получаем наименование валюты"""
    return operation['operationAmount']["currency"]["name"]
    # operationAmount = operation.get('operationAmount')
    # values = list(operationAmount.values())
    # currency = values[1]
    # currency_values = list(currency.values())[0]
    # return currency_values
