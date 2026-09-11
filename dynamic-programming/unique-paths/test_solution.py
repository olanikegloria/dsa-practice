from solution import Solution

def test_example():
    assert Solution().uniquePaths(3, 7) == 28

def test_square():
    assert Solution().uniquePaths(3, 2) == 3
