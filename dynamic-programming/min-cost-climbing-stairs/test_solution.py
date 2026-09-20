from solution import Solution

def test_example():
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15

def test_two():
    assert Solution().minCostClimbingStairs([10, 15]) == 10
