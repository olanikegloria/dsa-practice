from solution import Solution

def test_example():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    assert Solution().minPathSum([row[:] for row in grid]) == 7
