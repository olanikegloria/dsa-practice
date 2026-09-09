from solution import Solution

def test_example():
    assert Solution().coinChange([1,2,5], 11) == 3

def test_impossible():
    assert Solution().coinChange([2], 3) == -1

def test_zero():
    assert Solution().coinChange([2], 0) == 0
