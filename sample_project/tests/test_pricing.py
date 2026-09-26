from sample_project.invoice import price_total


def test_price_total_applies_discount_to_each_line():
    assert price_total([100.0, 50.0], 10.0) == 135.0


def test_zero_discount_preserves_the_total():
    assert price_total([12.5, 7.5], 0.0) == 20.0
