from um import count

def test_wtv():
    assert count("um?") == 1
    assert count("um, ana reem, um, ezayak ya mohamed ya zeft") == 2
    assert count("uhm, ezayek enti ya zeftet el zeft") == 0
    assert count("ya reeum tabkhek yummy gedannn yummmm") == 0


def test_wtv2():
    assert count("ummmmm, im reem and im stupid") == 0

def test_wtv3():
    assert count("Um hum Um um") == 3
