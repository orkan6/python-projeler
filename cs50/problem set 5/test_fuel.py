from fuel import gauge,convert
import pytest

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(45) == "45%"


def test_convert():
    assert convert("50/100") == 50
    assert convert("1/2") == 50
    assert convert("100/100") == 100

    with pytest.raises(ZeroDivisionError):
        assert convert("100/0")

    with pytest.raises(ValueError):
        assert convert("three/four")
