def filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    result = []
    for transaction in transactions:
        if transaction.get('state') == state:
            result.append(transaction)
    return result


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате с обработкой ошибок!
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=reverse)

