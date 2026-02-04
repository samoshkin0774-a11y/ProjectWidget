import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    'input_string, result',
    [
        ('Visa Platinum 7000792289606361','Visa Platinum 7000 79** **** 6361'),
        ('счет 73654108430135874305','счет **4305')
    ]
)
def test_mask_account_card(input_string, result):
    assert mask_account_card(input_string) == result

def test_get_date():
    assert get_date("2019-07-03T18:35:29.512364") == "03.07.2019"