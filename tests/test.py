from hypothesis import given, settings, strategies as st
import pytest

@given(
    st.lists(
        st.integers(min_value = -50, max_value = 100),
        min_size = 1,
        max_size = 100
    )
)
@settings(max_examples = 10)
def test_sorted_function(list):
    sorted_list = sorted(list)

    assert len(list) == len(sorted_list)

    assert set(list) == set(sorted_list)

    assert all(
        sorted_list[i] <= sorted_list[i + 1]
        for i in range(len(sorted_list) - 1)
    )
