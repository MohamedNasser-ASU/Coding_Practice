import pytest
from working import convert

def test_noMin():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_Min():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_error():
    with pytest.raises(ValueError):
        convert("9:61 am to 12:30 PM")
    with pytest.raises(ValueError):
        convert("9:61 am 12:30 PM")
    with pytest.raises(ValueError):
        convert("90:861 AM to 122:30 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 5 PM")
