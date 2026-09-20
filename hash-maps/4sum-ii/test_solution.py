from solution import Solution

def test_example():
    assert Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2

def test_zero():
    assert Solution().fourSumCount([0], [0], [0], [0]) == 1
