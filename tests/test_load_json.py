# -*- coding: utf-8 -*-

import pytest
from load_json import load_json, search_for_errors, removees_canceled, date_correction, sorting


def test_load_correct_json():
    test_list = load_json('operations.json')
    assert isinstance(test_list, list)


def test_search_for_errors():
    data = [{}, {'state': 'element'}, {'data': 'all'}]
    test_list = search_for_errors(data)
    assert test_list == [{'state': 'element'}]


def test_removees_canceled():
    data = load_json('operations.json')
    data = search_for_errors(data)
    state = "CANCELED"
    test_list = removees_canceled(data, state)
    assert test_list[1]['state'] == 'CANCELED'


def test_date_correction():
    date = [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    test_list = date_correction(date)
    assert test_list == [{'id': 615064591, 'state': 'CANCELED', 'date': '14.10.2018'}]


def test_sorting():
    data = [{'date': '14.10.2018'}, {'date': '10.10.2018'}, {'date': '10.07.2054'}]
    test_list = sorting(data)
    assert test_list == [{'date': '10.10.2018'}, {'date': '14.10.2018'}, {'date': '10.07.2054'}]
