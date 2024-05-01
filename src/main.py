import json
from functions import (load_operations,
                       executed_operations,
                       sort_date, get_date, get_description,
                       get_to, get_from_, get_amount, get_currency)

def main():
    # list_total = load_operations()
    # list_total_executed = executed_operations(list_total)
    # sorted_list_total_executed = sort_date(list_total_executed)
    sorted_list_total_executed = sort_date(executed_operations(load_operations()))
    for i in range(5):
        cur_op = sorted_list_total_executed[i]
        if get_from_(cur_op) == None:
            print(f"{get_date(cur_op)} {get_description(cur_op)}\n{get_to(cur_op)}\n{get_amount(cur_op)} {get_currency(cur_op)}\n")
        else:
            print(f"{get_date(cur_op)} {get_description(cur_op)}\n{get_from_(cur_op)} -> {get_to(cur_op)}\n{get_amount(cur_op)} {get_currency(cur_op)}\n")

main()