import json
import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_log_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)
logger = logging.getLogger("utils")
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def transaction_returner(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла со списком словарей и возвращает список словарей, как объект python.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    returned_list = []
    try:
        logger.info("Начал выгрузку с файла")
        with open(path, encoding="utf-8") as json_file:
            content = json.load(json_file)
            if isinstance(content, list):
                returned_list = content
        logger.info("Окончил выгрузку с файла")
    finally:
        return returned_list
