from solution import Solution

def test_add():
    assert Solution().calculate("1 + 1") == 2

def test_paren():
    assert Solution().calculate("(1+(4+5+2)-3)+6") == 15
