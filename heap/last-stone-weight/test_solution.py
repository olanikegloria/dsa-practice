from solution import Solution

def test_example():
    assert Solution().lastStoneWeight([2,7,4,1,8,1]) == 1

def test_single():
    assert Solution().lastStoneWeight([1]) == 1
