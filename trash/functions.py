def get_date(i):
    date_0 = s[i]['date'].split("T")
    date = ".".join(date_0[0].split("-")[::-1])
    return date


def get_description(i):
    description = s[i].get('description')
    return description


def get_from_(i):
    from_ = s[i].get("from")
    if from_ != None:
        return from_


def get_to(i):
    to = s[i].get("to")
    return to


def get_amount(i):
    operationAmount = s[i].get('operationAmount')
    values = list(operationAmount.values())
    amount = values[0]
    return amount


def get_currency(i):
    operationAmount = s[i].get('operationAmount')
    values = list(operationAmount.values())
    currency = values[1]
    currency_values = list(currency.values())[0]
    return currency_values
