from solution import Solution

def test_example():
    assert Solution().missingNumber([3, 0, 1]) == 2

def test_zero():
    assert Solution().missingNumber([1]) == 0
