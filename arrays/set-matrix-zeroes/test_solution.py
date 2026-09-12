from solution import Solution

def test_example():
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(m)
    assert m == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
