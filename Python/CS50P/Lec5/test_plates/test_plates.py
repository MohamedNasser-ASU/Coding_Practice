from plates import is_valid

def test_allAlpha():

    assert is_valid("CSFIFTY") == False
    assert is_valid("CSFIVE") == True
    assert is_valid("WORD") == True

def test_allNum():
    assert is_valid("50") == False
    assert is_valid("971CS") == False
    assert is_valid("123456") == False


def test_mix():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS6h1") == False
    assert is_valid("CS55555") == False
    assert is_valid("HELLO4") == True

def test_puncituation():
    assert is_valid("CS50.") == False


