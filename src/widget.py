def mask_account_card(input_string: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа

    """
    # Разделяем строку на части
    parts = input_string.split()

    # Определяем тип (первые слова до номера)
    account_type = " ".join(parts[:-1])
    number = parts[-1]

    # Проверяем, является ли это счетом
    if "счет" in account_type.lower() or "Счет" in account_type:
        # Маскировка для счета
        masked_number = f"**{number[-4:]}"
        return f"{account_type} {masked_number}"
    else:
        # Маскировка для карты
        if len(number) < 16:
            return input_string  # Неверный формат номера карты

        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        return f"{account_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ

    Args:
        date_string (str): Дата в формате "2024-03-11T02:26:18.671407"

    Returns:
        str: Дата в формате "11.03.2024"
    """
    from datetime import datetime

    try:
        # Парсим дату из строки
        dt = datetime.fromisoformat(date_string.replace("Z", "+00:00"))

        # Форматируем в нужный формат
        return dt.strftime("%d.%m.%Y")
    except (ValueError, AttributeError):
        return date_string  # Возвращаем исходную строку при ошибке

    # Функции для тестирования


