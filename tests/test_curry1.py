from hypothesis import given, settings, strategies as st
from src.curry import f
from src.curry import curry
from src.curry import uncurry
import pytest

def test_curry_base():

    @given(
        st.integers(),
        st.integers(),
        st.integers()
    )

    def test_three_args(x, y, z):
        f_curry = curry(f, 3)
        res_cur = f_curry(x)(y)(z)
        res = f(x, y, z)

        assert res_cur == res

def test_uncurry_base():
    @given(
        st.integers(),
        st.integers(),
        st.integers()
    )
    def test_three_args_uncurry(x, y, z):
        f_curry = curry(f, 3)
        f_uncurry = uncurry(f_curry, 3)
        res_uncur = f_uncurry(x, y, z)
        res = f(x, y, z)

        assert res_uncur == res

