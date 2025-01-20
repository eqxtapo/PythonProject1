import json


def transaction_returner(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла со списком словарей и возвращает список словарей, как объект python.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    returned_list = []
    try:
        with open(path, encoding="utf-8") as json_file:
            content = json.load(json_file)
            if isinstance(content, list):
                returned_list = content
    finally:
        return returned_list
