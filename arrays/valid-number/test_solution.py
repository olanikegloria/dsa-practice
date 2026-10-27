from solution import Solution

def test_zero():
    assert Solution().isNumber("0") is True

def test_e_invalid():
    assert Solution().isNumber("e") is False

def test_decimal():
    assert Solution().isNumber("0.1") is True
