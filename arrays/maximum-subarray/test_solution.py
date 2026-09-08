from solution import Solution

def test_example():
    assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_all_negative():
    assert Solution().maxSubArray([-3,-1,-2]) == -1
