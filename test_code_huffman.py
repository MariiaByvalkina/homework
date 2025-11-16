import pytest
from collections import Counter
from code_huffman import encode, decode


def test_encode_decode_simple():
    text = "a"
    encoded, table = encode(text)
    decoded = decode(encoded, table)
    assert text == decoded

def test_encode_decode_hello():
    text = "hello"
    encoded, table = encode(text)
    decoded = decode(encoded, table)
    assert text == decoded

def test_encode_decode_with_spaces():
    text = "hello world"
    encoded, table = encode(text)
    decoded = decode(encoded, table)
    assert text == decoded

def test_single_character():
    text = "aaaa"
    encoded, table = encode(text)
    decoded = decode(encoded, table)
    assert text == decoded
