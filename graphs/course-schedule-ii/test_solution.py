from solution import Solution

def test_example():
    assert Solution().findOrder(2, [[1,0]]) == [0,1]

def test_cycle():
    assert Solution().findOrder(2, [[1,0],[0,1]]) == []
