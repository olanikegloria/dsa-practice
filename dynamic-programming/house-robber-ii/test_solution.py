from solution import Solution

def test_example():
    assert Solution().rob([2,3,2]) == 3

def test_circle():
    assert Solution().rob([1,2,3,1]) == 4
