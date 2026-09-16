from solution import Solution

def test_example():
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    assert Solution().numIslands([row[:] for row in grid]) == 1

def test_two():
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    assert Solution().numIslands([row[:] for row in grid]) == 3
