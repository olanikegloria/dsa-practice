from solution import Solution

def test_example():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
