from src.widget import get_date, mask_accaunt_card

# Вызов функций
if __name__ == "__main__":
    print(mask_accaunt_card("Maestro 1596837868705199"))
    print(mask_accaunt_card("Счет 64686473678894779589"))
    print(mask_accaunt_card("MasterCard 7158300734726758"))
    print(mask_accaunt_card("Счет 35383033474447895560"))
    print(mask_accaunt_card("Visa Classic 6831982476737658"))
    print(mask_accaunt_card("Visa Platinum 8990922113665229"))
    print(mask_accaunt_card("Visa Gold 5999414228426353"))
    print(mask_accaunt_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
