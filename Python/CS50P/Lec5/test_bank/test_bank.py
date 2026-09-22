from bank import value

def test_word():
    assert value("hello") == 0
    assert value("hello mohamed") == 0
    assert value("hi reem") == 20
    assert value("Reemmmmm") == 100
    assert value("HellOReemmmmm") == 0


def test_num_punc():
    assert value("hel.lo1") == 20
    assert value("2?") == 100
