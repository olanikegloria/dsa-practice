from solution import Solution

def test_example():
    assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

def test_flat():
    assert Solution().trap([1,1,1]) == 0
