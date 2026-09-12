from solution import Solution

def test_found():
    m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert Solution().searchMatrix(m, 3) is True

def test_missing():
    m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert Solution().searchMatrix(m, 13) is False
