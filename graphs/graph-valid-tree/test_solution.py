from solution import Solution

def test_valid():
    assert Solution().validTree(5, [[0,1],[0,2],[0,3],[1,4]]) is True

def test_cycle():
    assert Solution().validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]) is False
