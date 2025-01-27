import re
from collections import Counter
from typing import Any

input_dict = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(input_dict: list[dict[str, Any]], state_id: str = "EXECUTED") -> list[dict[str, Any]]:
    """ Функция принимает список словарей, проверяет по ключу "state" и выдает новый список словарей в которых
     указан требуемый ключ """
    new_dict = []
    for key in input_dict:
        if key.get("state") == state_id:
            new_dict.append(key)
    return new_dict


def sort_by_date(input_dict: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """ Функция принимает список словарей и параметр, задающий порядок сортировки. Выдает отсортированный
    по дате список словарей. """
    sorted_by_date = sorted(input_dict, key=lambda x: x["date"], reverse=reverse)
    return sorted_by_date


def filter_by_description(transaction_list: list[dict], search_value: str) -> list[dict]:
    """Принимает список словарей и строковое значение. Возвращает список словарей, у которых ключ description
    соответствует строке из второго аргумента"""
    returned_list = []
    for transaction in transaction_list:
        if re.search(search_value, transaction["description"], flags=re.IGNORECASE):
            returned_list.append(transaction)
    return returned_list


def counter_by_description(transaction_list: list[dict], description_list: list[str]) -> dict:
    """Принимает на вход список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""
    list_for_requirement = []
    for description in description_list:
        for transaction in transaction_list:
            if transaction["description"] == description.title():
                list_for_requirement.append(transaction["description"])
    returned_dict = Counter(list_for_requirement)
    return returned_dict
