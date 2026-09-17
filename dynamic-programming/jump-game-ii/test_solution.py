from solution import Solution

def test_example():
    assert Solution().jump([2, 3, 1, 1, 4]) == 2

def test_single():
    assert Solution().jump([0]) == 0
