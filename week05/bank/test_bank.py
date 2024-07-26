from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("Hello, Norwan") == 0

def test_h():
    assert value("How you doing?") == 20

def test_hundred():
    assert value("What's happening?") == 100
