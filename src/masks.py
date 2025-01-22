import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_log_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)
logger = logging.getLogger("masks")
file_handler = logging.FileHandler(abs_log_file_path, 'w', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """ Функция маскирует номер карты, заменяя 7-12 цифры на '*' """
    if len(card_number) == 16:
        logger.info("Начали маскировку карты")
        mask_card_number = card_number[0:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]
        logger.info("Маскировка карты закончена")
        return mask_card_number
    else:
        logger.error("Неверный формат банковской карты")
        return "Неверный формат банковской карты"


def get_mask_account(account_number: str) -> str:
    """ Функция маскирует номер аккаунта, оставляя последние 4 цифры"""
    if len(account_number) == 20:
        logger.info("Начали маскировку номера счета")
        mask_account = "**" + account_number[-4:]
        logger.info("Маскировка номера счета закончена")
        return mask_account
    else:
        logger.error("Неверный формат номера счета")
        return "Неверный формат номера счета"
