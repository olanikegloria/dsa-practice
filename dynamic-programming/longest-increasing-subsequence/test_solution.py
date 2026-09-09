from solution import Solution

def test_example():
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_decreasing():
    assert Solution().lengthOfLIS([7, 7, 7, 7]) == 1
