from solution import Solution

def test_example():
    assert Solution().rob([1, 2, 3, 1]) == 4

def test_single():
    assert Solution().rob([2]) == 2
