from solution import Solution

def test_example():
    assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]

def test_with_zero():
    assert Solution().productExceptSelf([0,1,2]) == [2,0,0]
