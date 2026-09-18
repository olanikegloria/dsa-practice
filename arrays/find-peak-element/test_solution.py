from solution import Solution

def test_peak():
    assert Solution().findPeakElement([1, 2, 3, 1]) == 2

def test_two():
    assert Solution().findPeakElement([1, 2]) == 1
