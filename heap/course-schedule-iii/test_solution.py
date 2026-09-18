from solution import Solution

def test_example():
    assert Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3

def test_zero():
    assert Solution().scheduleCourse([[1, 2]]) == 1
