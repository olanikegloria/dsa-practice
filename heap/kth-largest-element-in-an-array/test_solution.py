from solution import Solution

def test_example():
    assert Solution().findKthLargest([3,2,1,5,6,4], 2) == 5

def test_k1():
    assert Solution().findKthLargest([1], 1) == 1
