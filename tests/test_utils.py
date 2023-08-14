# -*- coding: utf-8 -*-

import pytest

from load_json import sorting
from utils import get_five_operations, hide_symbols


def test_get_five_operations():
    yt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    test_list = get_five_operations(yt)
    assert test_list == [9, 8, 7, 6, 5]


def test_hide_symbols():
    data = [{'id': 594226727, 'state': 'CANCELED', 'date': '19.11.2019', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'},
            {'id': 476991061, 'state': 'CANCELED', 'date': '07.12.2019', 'operationAmount': {'amount': '26971.25', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Gold 7305799447374042', 'to': 'Maestro 3364923093037194'},
            {'id': 970724427, 'state': 'CANCELED', 'date': '08.12.2019', 'operationAmount': {'amount': '90688.44', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 2241653116508487', 'to': 'Счет 26494285169417058486'}]
    operations = sorting(data)
    test_list = hide_symbols(operations)
    assert  test_list == [{'id': 594226727, 'state': 'CANCELED', 'date': '19.11.2019', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246 37** **** 3588', 'to': 'Счет **1657'}, {'id': 476991061, 'state': 'CANCELED', 'date': '07.12.2019', 'operationAmount': {'amount': '26971.25', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Gold 7305 79** **** 4042', 'to': 'Maestro 3364 92** **** 7194'}, {'id': 970724427, 'state': 'CANCELED', 'date': '08.12.2019', 'operationAmount': {'amount': '90688.44', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 2241 65** **** 8487', 'to': 'Счет **8486'}]
