from solution import Solution

def test_example():
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10

def test_single():
    assert Solution().largestRectangleArea([2]) == 2
