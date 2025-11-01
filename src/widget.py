from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_string: str) -> str:
    """
    Маскируем номер карты или счета в зависимости

    """
    # Разделяем строку на части
    parts = input_string.split()

    # Определяем тип
    account_type = " ".join(parts[:-1])
    number = parts[-1]

    # Проверяем, является ли это счетом.
    if "счет" in account_type.lower() :

        return f"счет {get_mask_account(number)}"
    else:
        return f"{account_type} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """
    Преобразуем дату из формата ISO в формат ДД.ММ.ГГГГ

    """
    from datetime import datetime

    dt = datetime.fromisoformat(date_string.replace("Z", "+00:00"))

    return dt.strftime("%d.%m.%Y")

