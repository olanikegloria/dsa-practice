from solution import Solution

def test_example():
    assert Solution().findTargetSumWays([1,1,1,1,1], 3) == 5

def test_zero():
    assert Solution().findTargetSumWays([1], 1) == 1
