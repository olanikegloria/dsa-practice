from solution import Solution

def test_found():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert Solution().exist(board, "ABCCED") is True

def test_missing():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert Solution().exist(board, "ABCB") is False
