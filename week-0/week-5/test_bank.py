from bank import value

def test_zero():
    assert value("hello world") == 0
    assert value("HELLO !") == 0

def test_twenty():
    assert value("hi there") == 20
    assert value("hola senore") == 20

def test_hundred():
    assert value("Nice to meet you") == 100
    assert value("I am CS50 DUCK the debugger") == 100




