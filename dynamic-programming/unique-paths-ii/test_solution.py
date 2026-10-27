from solution import Solution

def test_grid():
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert Solution().uniquePathsWithObstacles(grid) == 2

def test_blocked_start():
    assert Solution().uniquePathsWithObstacles([[1]]) == 0
