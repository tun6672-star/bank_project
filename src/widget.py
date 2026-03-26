"""
Модуль с функциями-виджетами для работы с данными.
"""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """
    Принимает строку с типом и номером карты/счета.
    Возвращает строку с замаскированным номером.
    """
    parts = account_info.split()
    number = parts[-1]
    card_type = " ".join(parts[:-1])

    if len(number) == 16 and number.isdigit():
        masked_number = get_mask_card_number(number)
    elif len(number) == 20 and number.isdigit():
        masked_number = get_mask_account(number)
    else:
        return account_info
    return f"{card_type} {masked_number}"
