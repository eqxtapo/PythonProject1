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
