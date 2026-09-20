from solution import Solution

def test_up_down():
    assert Solution().candy([1, 0, 2]) == 5

def test_plateau():
    assert Solution().candy([1, 2, 2]) == 4
