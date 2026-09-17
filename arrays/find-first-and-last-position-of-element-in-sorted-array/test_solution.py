from solution import Solution

def test_range():
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]

def test_missing():
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
