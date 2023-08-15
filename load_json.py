# -*- coding: utf-8 -*-

import json
from datetime import datetime


def load_json(filename):
    """Читает json-файл и возвращает файл со словарями"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)


def search_for_errors(data):
    """Создаёт новый список словарей, фильтруя данные по наличию ключа 'state', и возвращает его"""
    operations = []
    for element in data:
        if 'state' in element:
            operations.append(element)
    return operations


def removees_canceled(data, state):
    """Создаёт новый список словарей, фильтруя данные по значению ключа 'state', и возвращает его"""
    operetions = []
    for element in data:
        if element['state'] == state:
            operetions.append(element)
    return operetions


def date_correction(data):
    """Создаёт новый список словарей, меняя формат даты в исходном, и возвращает новый список"""
    operations = []
    for element in data:
        date = datetime.strptime(element['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        element['date'] = date
        operations.append(element)
    return operations


def sorting(data):
    """Сортирует список по дате операции и возвращает его"""
    return sorted(data, key=lambda e: '.'.join(reversed(e['date'].split('.'))))
