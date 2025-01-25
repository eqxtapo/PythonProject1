import csv

import pandas as pd


def csv_reader(path: str) -> list[dict]:
    """Принимает на вход путь к файлу csv. Возвращает список словарей из файла"""
    returned_list = []
    try:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            print(reader)
            for row in reader:
                returned_list.append(row)
    finally:
        return returned_list


def excel_reader(path: str) -> list[dict]:
    """Принимает на вход путь к файлу excel. Возвращает список словарей из файла"""
    returned_list = []
    try:
        reader = pd.read_excel(path)
        returned_list = reader.to_dict(orient="records")
    finally:
        return returned_list
