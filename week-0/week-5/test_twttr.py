from twttr import shorten

def test_lowerCase():
    assert shorten("twitter") == "twttr"
    assert shorten("banana") == "bnn"
    assert shorten("football") == "ftbll"
    assert shorten("hello!") == "hll!"

def test_upperCase():
    assert shorten("TWitTer") == "TWtTr"
    assert shorten("BanaNA") == "BnN"
    assert shorten("FOOTball") == "FTbll"

def test_digits():
    assert shorten("23") == "23"
    assert shorten("-23") == "-23"
    assert shorten("0") == "0"

