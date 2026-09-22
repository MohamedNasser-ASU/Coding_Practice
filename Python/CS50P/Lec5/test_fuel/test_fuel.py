import pytest

from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


def test_value_error():
    with pytest.raises(ValueError):
        convert("4/3")

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("-1/4")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
