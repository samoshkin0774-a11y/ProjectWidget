import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567890123458") == "1234 56** **** 3458"
    assert get_mask_card_number("3555") == "Некорректный номер карты"
    assert get_mask_card_number("700079228960636f") == "Некорректный номер карты"

def test_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("1234567890") == "**7890"
    assert get_mask_account("123") == "Номер счета должен содержать минимум 4 цифры"
    assert get_mask_account("7365410e430135874305") == "Номер счета должен содержать минимум 4 цифры"
