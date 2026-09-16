from solution import Solution

def test_example():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    assert Solution().maximalSquare(matrix) == 4
