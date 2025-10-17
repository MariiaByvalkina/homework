from src.heap_sort import heap_sort

import pytest

def test_sort_even_count_heap():
    arr = [10, 20, 15, 30, 40, 35, 12, 25]
    result = [10, 12, 15, 20, 25, 30, 35, 40]
    assert heap_sort(arr) == result

def test_empty_arr():
    arr = []
    assert heap_sort(arr) == arr

def test_single_arr():
    arr = [5]
    assert heap_sort(arr) == arr


