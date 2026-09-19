from solution import Solution

def test_example():
    assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3

def test_impossible():
    assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
