import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567890123458") == "1234 56** **** 3458"


def test_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("1234567890") == "**7890"


def test_mask_card_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number("12345")  # Слишком короткий номер
    with pytest.raises(ValueError):
        get_mask_card_number("abcdefghijklmno")  # Не цифры


def test_mask_account_invalid():
    with pytest.raises(ValueError):
        get_mask_account("123")  # Слишком короткий номер
    with pytest.raises(ValueError):
        get_mask_account("abcde")  # Не цифры
