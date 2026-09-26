from calculator import add, multiply, subtract


def test_add_two_numbers():
    assert add(2, 3) == 5


def test_subtract_two_numbers():
    assert subtract(10, 4) == 6


def test_multiply_two_numbers():
    assert multiply(6, 7) == 42
