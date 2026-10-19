import pytest

from leap import is_leap


def test_2024_is_a_leap_year():
    assert is_leap(2024)


def test_1900_is_not_a_leap_year():
    assert not is_leap(1900)


@pytest.mark.parametrize("year, expected", [
    (2000, True),   # Divisible by 400.
    (1900, False),  # Divisible by 100, but not by 400.
    (2024, True),   # Divisible by 4, but not by 100.
    (2023, False),  # Not divisible by 4.
    (2400, True),   # Additional row: divisible by 400.
    (2100, False),  # Additional row: divisible by 100, not by 400.
])
def test_is_leap(year, expected):
    assert is_leap(year) == expected
