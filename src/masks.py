"""
Модуль с функциями маскировки номеров карт и счетов.
"""


def get_mask_card_number(card_number: str) -> str:
    """Принимает номер карты (строка из 16 цифр) и возвращает его маску."""
    if len(card_number) != 16 or not card_number.isdigit():
        return "Неверный формат номера карты"

    masked_part = card_number[6:12]
    masked_number = card_number[:6] + "*" * len(masked_part) + card_number[-4:]

    result = " ".join(masked_number[i : i + 4] for i in range(0, len(masked_number), 4))
    return result


def get_mask_account(account_number: str) -> str:
    """Принимает номер счета (строка из 20 цифр) и возвращает его маску."""
    if not account_number.isdigit():
        return "Неверный формат номера счета"

    return f"**{account_number[-4:]}"
