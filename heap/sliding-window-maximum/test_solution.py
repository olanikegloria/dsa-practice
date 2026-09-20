from solution import Solution

def test_example():
    assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

def test_single():
    assert Solution().maxSlidingWindow([1], 1) == [1]
