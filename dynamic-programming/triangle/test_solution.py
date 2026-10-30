from solution import Solution

def test_example():
    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    assert Solution().minimumTotal(tri) == 11

def test_single():
    assert Solution().minimumTotal([[-10]]) == -10
