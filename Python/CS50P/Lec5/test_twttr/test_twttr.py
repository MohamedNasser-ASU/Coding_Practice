from twttr import shorten

def test_word():
    assert shorten("HEllo") == "Hll"
    assert shorten("reem") == "rm"

def test_num():
    assert shorten("He11o") == "H11"
def test_punc():
    assert shorten("He11o.") == "H11."
