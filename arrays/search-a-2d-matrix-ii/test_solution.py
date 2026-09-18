from solution import Solution

def test_found():
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    assert Solution().searchMatrix(matrix, 5) is True

def test_missing():
    matrix = [[1, 4], [2, 5]]
    assert Solution().searchMatrix(matrix, 3) is False
