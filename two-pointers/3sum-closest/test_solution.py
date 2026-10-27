from solution import Solution

def test_example():
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2

def test_exact():
    assert Solution().threeSumClosest([0, 0, 0], 1) == 0
