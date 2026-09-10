from solution import Solution

def test_example():
    assert Solution().leastInterval(["A","A","A","B","B","B"], 2) == 8

def test_no_idle():
    assert Solution().leastInterval(["A","A","A","B","B","B"], 0) == 6
