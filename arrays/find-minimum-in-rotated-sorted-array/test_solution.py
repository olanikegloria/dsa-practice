from solution import Solution

def test_example():
    assert Solution().findMin([3, 4, 5, 1, 2]) == 1

def test_no_rotation():
    assert Solution().findMin([1, 2, 3, 4, 5]) == 1
