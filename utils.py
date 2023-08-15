# -*- coding: utf-8 -*-

def get_five_operations(sort):
    """Возвращает пять последних операций в порядке от последней, по дате"""
    sort = sort[-5:]
    sort.reverse()
    return sort


#
def hide_symbols(operations):
    """Маскирует символы в операциях пользователя, проверяя первый символ в значении словаря"""

    for element in operations:
        if element['to'][0] == 'С':
            element['to'] = 'Счет ' + '**' + element['to'][-4:]
        else:
            element['to'] = element['to'][:-12] + ' ' + element['to'][-12:-10] + '** ' + '**** ' + element['to'][-4:]
        if 'from' in element:
            if element['from'][0] == 'С':
                element['from'] = 'Счет ' + '**' + element['from'][-4:]
            else:
                element['from'] = element['from'][:-12] + ' ' + element['from'][-12:-10] + '** ' + '**** ' + element[
                                                                                                                'from'][
                                                                                                            -4:]
        else:
            continue

    return operations
