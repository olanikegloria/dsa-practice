from solution import Solution

def test_single():
    assert Solution().numOfMinutes(1, 0, [-1], [0]) == 0

def test_chain():
    assert Solution().numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]) == 1
