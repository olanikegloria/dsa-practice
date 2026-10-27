from solution import Solution

def test_three():
    assert Solution().generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

def test_one():
    assert Solution().generateMatrix(1) == [[1]]
