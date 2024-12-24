import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("value, expected", [
    ("1234567890987654", "1234 56** **** 7654"),
    ("4573568243563457", "4573 56** **** 3457"),
    ("9679466735674584", "9679 46** **** 4584"),
    ("3455674568323456", "3455 67** **** 3456"),
    ("4678923456467893", "4678 92** **** 7893"),
    ("4435556754682334", "4435 55** **** 2334"),
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("73654108430135874305", "**4305"),
    ("43563457634567345687", "**5687"),
    ("45684567345634578655", "**8655"),
    ("34679347859072340954", "**0954"),
    ("23904823907593481232", "**1232"),
    ("32740958723849075345", "**5345"),
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
