def get_mask_card_number(card_number: str) -> str:
    """ Функция маскирует номер карты, заменяя 7-12 цифры на '*' """
    return card_number[0:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]


def get_mask_account(accaunt_number: str) -> str:
    """ Функция маскирует номер аккаунта, оставляя последние 4 цифры"""
    return "**" + accaunt_number[-4:]
