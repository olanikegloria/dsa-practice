from solution import Solution

def test_example():
    assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49

def test_two_bars():
    assert Solution().maxArea([1,1]) == 1
