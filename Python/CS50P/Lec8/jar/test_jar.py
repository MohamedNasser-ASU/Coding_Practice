from jar import Jar
import pytest


def test_init():
    jar = Jar()

    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()

    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar()

    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(2)
    assert jar.size == 7

    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    jar.withdraw(2)

    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)


def test_capacity():
    jar = Jar(5)

    assert jar.capacity == 5

    with pytest.raises(ValueError):
        Jar(-1)
