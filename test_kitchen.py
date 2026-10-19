# Test list (checked only after a corresponding test passes):
# [x] 200 g x 3 = 600 g
# [ ] Multiplication does not modify the original
# [ ] Equal amount and unit means equal quantities
# [ ] 1 oz is not the same as 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz reduced to grams using a rate
# [ ] (200 g + 1 oz) x 2

from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200)
    flour.times(3)
    assert flour.amount == 600


def test_multiplication_by_two():
    flour = Quantity(200)
    flour.times(2)
    assert flour.amount == 400
