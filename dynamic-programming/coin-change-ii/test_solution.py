from solution import Solution

def test_example():
    assert Solution().change(5, [1,2,5]) == 4

def test_zero():
    assert Solution().change(3, [2]) == 0
