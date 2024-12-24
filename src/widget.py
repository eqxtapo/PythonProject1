from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция обрабатывает информацию о картах и счетах, частично маскируя их """
    if "счет" in card_info.lower():
        return "Счет" + " " + get_mask_account(card_info)
    else:
        splited = card_info.split()
        return " ".join(splited[:-1]) + " " + get_mask_card_number(splited[-1])


def get_date(date_info: str) -> str:
    """Функция обрабатывает информацию о дате, возвращая её в ином формате"""
    date = date_info.split('T')[0]
    year, month, day = date.split('-')
    return f'{day}.{month}.{year}'
