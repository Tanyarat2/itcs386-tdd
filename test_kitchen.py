# Test list (checked only after a corresponding test passes):
# [x] 200 g x 3 = 600 g
# [x] Multiplication does not modify the original
# [x] Equal amount and unit means equal quantities
# [x] 1 oz is not the same as 1 g
# [x] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz reduced to grams using a rate
# [ ] (200 g + 1 oz) x 2

from kitchen import Converter, Quantity, grams, ounces


def test_multiplication():
    flour = grams(200)
    assert flour.times(3) == grams(600)


def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    assert flour.times(3) == grams(600)
    assert flour.times(2) == grams(400)
    assert flour == grams(200)


def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)


# [ ] Deferred concern: hashability (not required by this lab).


def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)


def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)


def test_reduce_same_unit_needs_no_rate():
    converter = Converter()
    assert converter.reduce(grams(500), "g") == grams(500)
