from plates import is_valid

def test_start():
    assert is_valid("HELLO") == True
    assert is_valid("HELL50") == True
    assert is_valid("50HELL") == False
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("CS05") == False
    assert is_valid("50") == False
    assert is_valid("PI3.14") == False
    assert is_valid("CS50") == True
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("CS50P") == False


