from curry import curry
from curry import uncurry
from curry import f

import pytest

def test_curry_random():
    f_curry = curry(f, 3)
    x, y, z = 1, 2, 3
    res = 6
    assert f_curry(1)(2)(3) == res

def test_uncurry():
    f_curry = curry(f, 3)
    f_uncurry = uncurry(f_curry, 3)
    x, y, z = 1, 2, 3
    res = 6
    assert f_uncurry(1, 2, 3) == res
