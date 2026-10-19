# Test list (checked only after a corresponding test passes):
# [x] 200 g x 3 = 600 g
# [x] Multiplication does not modify the original
# [x] Equal amount and unit means equal quantities
# [x] 1 oz is not the same as 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz reduced to grams using a rate
# [ ] (200 g + 1 oz) x 2

from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200, "g")
    assert flour.times(3) == Quantity(600, "g")


def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200, "g")
    assert flour.times(3) == Quantity(600, "g")
    assert flour.times(2) == Quantity(400, "g")
    assert flour == Quantity(200, "g")


def test_equality():
    assert Quantity(200, "g") == Quantity(200, "g")
    assert Quantity(200, "g") != Quantity(300, "g")


# [ ] Deferred concern: hashability (not required by this lab).


def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")
