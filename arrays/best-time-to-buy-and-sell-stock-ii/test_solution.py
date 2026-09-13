from solution import Solution

def test_example():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7

def test_flat():
    assert Solution().maxProfit([1, 1, 1]) == 0
