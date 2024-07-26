from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(3)
    assert jar.capacity == 3
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar._size == 0
    jar.deposit(5)
    assert jar._size == 5
    jar.deposit(2)
    assert jar._size == 7


def test_withdraw():
    jar = Jar()
    assert jar._size == 0
    jar.deposit(7)
    jar.withdraw(2)
    assert jar._size == 5
    jar.withdraw(3)
    assert jar._size == 2
