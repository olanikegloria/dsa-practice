from solution import Solution

def test_true():
    assert Solution().canPartition([1,5,11,5]) is True

def test_false():
    assert Solution().canPartition([1,2,3,5]) is False
