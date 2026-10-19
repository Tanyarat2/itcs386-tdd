import pytest
from shipping import shipping_fee


# Rule 1 bug: zero must raise ValueError, just like a negative weight.
@pytest.mark.parametrize("weight", [-1, 0])
def test_nonpositive_weight_is_rejected(weight):
    with pytest.raises(ValueError, match="more than 0 kg"):
        shipping_fee(weight)


# Rule 2 bug: exactly 1 kg belongs to the 40-baht band.
@pytest.mark.parametrize("weight, expected", [(0.1, 40), (0.5, 40), (1, 40)])
def test_up_to_one_kg(weight, expected):
    assert shipping_fee(weight) == expected


@pytest.mark.parametrize("weight, expected", [(1.01, 60), (3, 60), (5, 60)])
def test_more_than_one_and_up_to_five_kg(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 4 bug: each started extra kilogram must round up, not truncate.
@pytest.mark.parametrize("weight, expected", [
    (5.01, 70), (5.2, 70), (6, 70), (6.01, 80), (7, 80),
])
def test_started_extra_kilograms(weight, expected):
    assert shipping_fee(weight) == expected
