from plates import is_valid

def test_two_letters():
    assert is_valid("H") == False
    assert is_valid("21DAYS") == False
    assert is_valid("50") == False

def test_length():
    assert is_valid("OUTATIME") == False

def test_numbers():
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("PI3.14") == False

def test_all():
    assert is_valid("CS50") == True
