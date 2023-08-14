# -*- coding: utf-8 -*-
from load_json import load_json, search_for_errors, removees_canceled, date_correction, sorting
from utils import hide_symbols, get_five_operations

FILENAME = 'operations.json'


def start_main():
    state = 'EXECUTED'
    data = load_json(FILENAME)
    data = search_for_errors(data)
    data = removees_canceled(data, state)
    data = date_correction(data)
    sort = sorting(data)
    operations = get_five_operations(sort)

    for element in hide_symbols(operations):
        print(f"{element['date']} {element['description']}")
        if 'from' in element:
            print(f"{element['from']} -> {element['to']}")
        else:
            print(element['to'])
        print(f"{element['operationAmount']['amount']} {element['operationAmount']['currency']['name']}")
        print()


if __name__ == "__main__":
    start_main()

