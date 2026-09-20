from solution import Solution

def test_example():
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2

def test_impossible():
    assert Solution().minSubArrayLen(100, [1, 2, 3]) == 0
