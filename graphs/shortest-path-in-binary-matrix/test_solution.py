from solution import Solution

def test_example():
    assert Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2

def test_blocked():
    assert Solution().shortestPathBinaryMatrix([[1, 0], [0, 0]]) == -1
