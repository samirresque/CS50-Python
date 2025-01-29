from fuel import convert, gauge
import pytest

def test_valid_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("9/10") == 90

def test_valid_gauge():
    assert gauge(90) == "90%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_invalid_convert():
    with pytest.raises(ValueError):
        convert("three/four")

    with pytest.raises(ZeroDivisionError):
        convert("4/0")




