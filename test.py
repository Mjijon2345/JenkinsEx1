# test.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 2) == 3
