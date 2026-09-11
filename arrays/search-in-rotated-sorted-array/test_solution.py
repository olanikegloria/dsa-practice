from solution import Solution

def test_example():
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4

def test_miss():
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1
