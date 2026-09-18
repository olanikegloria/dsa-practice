from solution import Solution

def test_matrix():
    assert Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4

def test_single():
    assert Solution().longestIncreasingPath([[1]]) == 1
