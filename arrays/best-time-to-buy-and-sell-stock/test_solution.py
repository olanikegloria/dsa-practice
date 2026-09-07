from solution import Solution

def test_example():
    assert Solution().maxProfit([7,1,5,3,6,4]) == 5

def test_decreasing():
    assert Solution().maxProfit([7,6,4,3,1]) == 0
