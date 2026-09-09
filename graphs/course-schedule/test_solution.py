from solution import Solution

def test_ok():
    assert Solution().canFinish(2, [[1, 0]]) is True

def test_cycle():
    assert Solution().canFinish(2, [[1, 0], [0, 1]]) is False
