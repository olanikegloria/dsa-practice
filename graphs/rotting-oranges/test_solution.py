from solution import Solution

def test_example():
    assert Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4

def test_impossible():
    assert Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
