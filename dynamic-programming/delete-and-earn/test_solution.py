from solution import Solution

def test_example():
    assert Solution().deleteAndEarn([3, 4, 2]) == 6

def test_all_same():
    assert Solution().deleteAndEarn([2, 2, 2]) == 6
