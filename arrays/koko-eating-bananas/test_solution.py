from solution import Solution

def test_piles():
    assert Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4

def test_equal_hours():
    assert Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
