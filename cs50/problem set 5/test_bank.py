from bank import value

def test_bank():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hi") == 20
    assert value("what's happening?") == 100



