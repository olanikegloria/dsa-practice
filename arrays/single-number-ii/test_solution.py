from solution import Solution

def test_2232():
    assert Solution().singleNumber([2, 2, 3, 2]) == 3

def test_negative():
    assert Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99
