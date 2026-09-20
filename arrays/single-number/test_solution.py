from solution import Solution

def test_small():
    assert Solution().singleNumber([2, 2, 1]) == 1

def test_larger():
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4
