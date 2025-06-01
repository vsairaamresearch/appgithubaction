from src.math_operations import add, sub

def test_add():
    assert add(1, 1) == 2
    assert add(2, -2) == 0

def test_sub():
    assert sub(1, -1) == 2
    assert sub(1, 1) == 0