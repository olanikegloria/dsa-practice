from solution import Solution

def test_example():
    assert set(Solution().topKFrequent([1,1,1,2,2,3], 2)) == {1,2}

def test_one():
    assert Solution().topKFrequent([1], 1) == [1]
