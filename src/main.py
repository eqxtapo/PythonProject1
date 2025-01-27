import os

from src.file_reader import csv_reader, excel_reader
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.utils import transaction_returner
from src.widget import get_date, mask_account_card


def main() -> None:
    """Отвечает за основную логику проекта и связывает функциональности между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print("""Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла""")
        type_of_file = input()
        if type_of_file == "1" or type_of_file.lower() == "json":
            descr_type_file = "JSON"
            transaction_list = transaction_returner(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data"
                                                    f"\\operations.json")
            break
        elif type_of_file == "2" or type_of_file.lower() == "csv":
            descr_type_file = "CSV"
            transaction_list = csv_reader(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data"
                                          f"\\transactions.csv")
            break
        elif type_of_file == "3" or type_of_file.lower() == "xlsx":
            descr_type_file = "XLSX"
            transaction_list = excel_reader(f"{os.path.join(os.path.dirname(__file__), os.pardir)}\\data"
                                            f"\\transactions_excel.xlsx")
            break
        else:
            print("Некорректный выбор пункта в меню. Необходимо выбрать один из предложенных вариантов")
    print(f"Для обработки выбран {descr_type_file}-файл.\n")
    while True:
        print("""Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        status_for_filter = input()
        status_for_filter = status_for_filter.upper()
        if status_for_filter == "EXECUTED" or status_for_filter == "CANCELED" or status_for_filter == "PENDING":
            print(f"Операции отфильтрованы по статусу {status_for_filter}")
            break
        else:
            print(f"Статус операции {status_for_filter} недоступен")
    transaction_list = filter_by_state(transaction_list, status_for_filter)
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        answer_for_date = input()
        if answer_for_date.lower() == "да" or answer_for_date.lower() == "yes":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                answer_for_order = input()
                if "возрастан" in answer_for_order.lower() or "убыван" in answer_for_order.lower():
                    order_for_date = (answer_for_order.lower == "по убыванию")
                    transaction_list = sort_by_date(transaction_list, order_for_date)
                    break
                else:
                    print("Выбор не распознан")
                    continue
            break
        elif answer_for_date.lower() == "нет" or answer_for_date.lower() == "no":
            break
        else:
            print("Ответ не распознан")
    while True:
        print("Выводить только рублевые тразакции? Да/Нет")
        answer_for_currency = input()
        if answer_for_currency.lower() == "да" or answer_for_currency.lower() == "yes":
            support_list = []
            if descr_type_file == "JSON":
                for transaction in transaction_list:
                    if transaction["operationAmount"]["currency"]["code"] == "RUB":
                        support_list.append(transaction)
            else:
                for transaction in transaction_list:
                    if transaction["currency_code"] == "RUB":
                        support_list.append(transaction)
            transaction_list = support_list
            break
        elif answer_for_currency.lower() == "нет" or answer_for_currency.lower() == "no":
            break
        else:
            print("Ответ не распознан")
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        answer_for_description = input()
        if answer_for_description.lower() == "да" or answer_for_description.lower() == "yes":
            print("Введите слово, по которому будем фильтровать список")
            user_description = input()
            transaction_list = filter_by_description(transaction_list, user_description)
            break
        elif answer_for_description.lower() == "нет" or answer_for_description.lower() == "no":
            break
        else:
            print("Ответ не распознан")
    print("Распечатываю итоговый список транзакций...\n")
    if len(transaction_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(transaction_list)}")
        if descr_type_file == "JSON":
            for transaction in transaction_list:
                if transaction["description"] == "Открытие вклада":
                    print(f"{get_date(transaction["date"])} {transaction["description"]}\n"
                          f"{mask_account_card(transaction["to"])}\nСумма: {transaction["operationAmount"]["amount"]} "
                          f"{transaction["operationAmount"]["currency"]["name"]}")
                else:
                    print(f"{get_date(transaction["date"])} {transaction["description"]}\n"
                          f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}\n"
                          f"Сумма: {transaction["operationAmount"]["amount"]} "
                          f"{transaction["operationAmount"]["currency"]["name"]}")
        else:
            for transaction in transaction_list:
                if transaction["currency_name"] == 'Ruble':
                    transaction["currency_name"] = "руб."
                if transaction["description"] == "Открытие вклада":
                    print(f"{get_date(transaction["date"])} {transaction["description"]}\n"
                          f"{mask_account_card(transaction["to"])}\nСумма: {transaction["amount"]} "
                          f"{transaction["currency_name"]}")
                else:
                    print(f"{get_date(transaction["date"])} {transaction["description"]}\n"
                          f"{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}\n"
                          f"Сумма: {transaction["amount"]} {transaction["currency_name"]}")
