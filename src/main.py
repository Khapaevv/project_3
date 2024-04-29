import json
from functions import get_date
from functions import get_description
from functions import get_to
from functions import get_from_
from functions import get_amount
from functions import get_currency

def main():
    for i in range(5):
        if get_from_(i) == None:
            print(f"{get_date(i)} {get_description(i)}\n{get_to(i)}\n{get_amount(i)} {get_currency(i)}\n")
        else:
            print(f"{get_date(i)} {get_description(i)}\n{get_from_(i)} -> {get_to(i)}\n{get_amount(i)} {get_currency(i)}\n")

main()