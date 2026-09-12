from solution import Solution

def test_happy():
    assert Solution().isHappy(19) is True

def test_unhappy():
    assert Solution().isHappy(2) is False
