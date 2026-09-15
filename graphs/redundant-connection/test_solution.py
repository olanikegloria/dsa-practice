from solution import Solution

def test_example():
    assert Solution().findRedundantConnection([[1,2],[1,3],[2,3]]) == [2,3]

def test_another():
    assert Solution().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1,4]
