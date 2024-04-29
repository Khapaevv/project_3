from src.functions import executed_operations
from src.functions import sort_date
from src.functions import get_date
from src.functions import load_operations
from src.functions import get_description
from src.functions import get_to
from src.functions import get_from_
from src.functions import get_amount
from src.functions import get_currency

def test_executed_operations():
    operations = [{'state': "EXECUTED"},
                  {'state': "EXEeeeTED"},
                  {'stateeee': "EXECUTED"},
                  {'state': "executed"},
                  {'state': "CANCELED"},
                  {}]
    assert executed_operations(operations) == [{'state': "EXECUTED"}]

def test_sort_date():
    dates = [{"date": "2019-12-08T22:46:21.935582"},
             {"date": "2019-08-08T22:46:21.935582"},
              {"date": "2017-12-08T22:46:21.935582"},
             {"date": "2019-12-08T20:46:21.935582"},
             {"date": "2019-12-08T22:09:21.935582"}]
    assert sort_date(dates) == [
        {"date": "2019-12-08T22:46:21.935582"},
        {"date": "2019-12-08T22:09:21.935582"},
        {"date": "2019-12-08T20:46:21.935582"},
        {"date": "2019-08-08T22:46:21.935582"},
        {"date": "2017-12-08T22:46:21.935582"}]


def test_get_date():
    date = {"date": "2017-12-08T22:46:21.935582"}
    assert get_date(date) == '08.12.2017'


def test_get_description():
    d = {"description": "Открытие вклада"}
    assert get_description(d) == "Открытие вклада"


def test_get_from_kart():
    kart = {"from": "Visa Platinum 1246377376343588"}
    assert get_from_(kart) == "Visa Platinum 1246 37** **** 3588"


def test_get_from_schet():
    schet = {"from": "Счет 90424923579946435907"}
    assert get_from_(schet) == "Счет **5907"


def test_get_to_kart():
    kart = {"to": "Visa Platinum 1246377376343588"}
    assert get_to(kart) == "Visa Platinum 1246 37** **** 3588"


def test_get_to_schet():
    schet = {"to": "Счет 90424923579946435907"}
    assert get_to(schet) == "Счет **5907"

def test_get_amount():
    amount = {"operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }}}
    assert get_amount(amount) == "41096.24"


def test_get_currency():
    currency = {"operationAmount": {
        "amount": "41096.24",
        "currency": {
            "name": "USD",
            "code": "USD"
        }}}
    assert get_currency(currency) == "USD"




