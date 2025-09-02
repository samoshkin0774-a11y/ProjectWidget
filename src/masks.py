def get_mask_card_number(card_number: str) -> str:
    """Маскируем номер банковской карты в формате XXXX XX** **** XXXX"""
    # Убираем все пробелы на случай, если номер пришел с ними
    card_number = card_number.replace(" ", "")

    # Проверяем, что номер состоит из 16 цифр
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    # Форматируем номер: первые 6 цифр + последние 4 цифры, остальное - звездочки
    masked_part = "** ****"
    return f"{card_number[:4]} {card_number[4:6]}{masked_part} {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскируем номер банковского счета в формате **XXXX"""
    # Убираем все пробелы
    account_number = account_number.replace(" ", "")

    # Проверяем, что номер счета состоит минимум из 4 цифр
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    # Показываем только последние 4 цифры
    return f"**{account_number[-4:]}"
