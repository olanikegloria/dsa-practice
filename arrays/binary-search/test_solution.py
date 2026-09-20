from solution import Solution

def test_found():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4

def test_missing():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1
