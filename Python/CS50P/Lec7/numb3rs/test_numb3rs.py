from numb3rs import validate

def test_valid():
    assert validate("1.1.1.1") == True
    assert validate("1.30.50.255") == True

def test_invalid():
    assert validate("275.581.1.1") == False
    assert validate("50.005.01.010") == False




