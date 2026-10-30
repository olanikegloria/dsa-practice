from solution import Solution

def test_example():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().gameOfLife(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
