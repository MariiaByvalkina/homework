import pytest
from src.walker import Walker

def test_empty_list():
    with pytest.raises(ValueError):
        Walker([])

def test_negative_probability():
    with pytest.raises(ValueError):
        Walker([("A", 0.5), ("B", -0.5)])

def test_sum_less_than_one():
    with pytest.raises(ValueError):
        Walker([("A", 0.5), ("B", 0.4)])

def test_one_event():
    walker = Walker([("A", 1.0)])
    assert walker.get_random() == "A"

def test_sum_greater():
    walker = Walker([("A", 0.6), ("B", 0.5)])
    assert walker.n == 2

    