from src.widget import mask_account_card, get_date


def test_functions():
    """Тестирование функций модуля"""

    # Тестовые данные
    global test_dates
    test_cases = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]

    print("Тестирование mask_account_card:")
    print("-" * 50)
    for case in test_cases:
        result = mask_account_card(case)
        print(f"Вход:  {case}")
        print(f"Выход: {result}")
        print()

        print("\nТестирование get_date:")
        print("-" * 30)
        test_dates = ["2024-03-11T02:26:18.671407", "2023-12-25T15:30:45.123456", "2022-06-01T08:00:00.000000"]

    for date in test_dates:
        result = get_date(date)
        print(f"Вход:  {date}")
        print(f"Выход: {result}")
        print()

    if __name__ == "__main__":
        test_functions()
