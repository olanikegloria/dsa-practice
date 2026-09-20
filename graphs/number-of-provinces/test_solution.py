from solution import Solution

def test_two():
    assert Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2

def test_one():
    assert Solution().findCircleNum([[1, 1], [1, 1]]) == 1
