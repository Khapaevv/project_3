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
    from_stars = from_[:-12] + '******' + from_[-6:]

    # if from_ == None:
    #     continue
    # else:
    #     from_w = from_[-10:-5]
    return from_stars



def get_to(i):
    """получаем кому и заменяем звездочками"""
    to = s[i].get("to")
    to_stars = to[:-12] + "******" + to[-6:]
    return to_stars


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
