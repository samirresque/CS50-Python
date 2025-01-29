from plates import is_valid

def test_valid_letters():
    #assert is_valid("CS") == True
    assert is_valid("VS") == True
    assert is_valid("HELLO") == True
    assert is_valid("Do") == True
    assert is_valid("AAA") == True

def test_valid_alphaNum():
    assert is_valid("CS50") == True
    assert is_valid("AAAA20") == True

def test_invalid_letters():
    assert is_valid("Z") == False
    assert is_valid("Hello, World") == False
    assert is_valid("Hi!") == False
    assert is_valid("GoodBye") == False

def test_invalid_alphaNum():
    assert is_valid("50CS") == False
    assert is_valid("AAA22A") == False
    assert is_valid("CS50!") == False
    assert is_valid("CS05") == False


