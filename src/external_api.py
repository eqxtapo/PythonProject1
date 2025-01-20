import os
from typing import Any

import requests
from dotenv import load_dotenv


def rubles_converter(transaction: dict) -> Any:
    amount = float(transaction["operationAmount"]["amount"])  # получение суммы траты
    currency = transaction["operationAmount"]["currency"]["code"]  # получение валюты
    if currency != "RUB":
        load_dotenv()
        API_KEY = os.getenv("API_TOKEN")
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"

        headers = {"apikey": f"{API_KEY}"}

        response = requests.get(url, headers=headers)

        return round(response.json()["rates"]["RUB"] * amount, 2)
    return amount
