from solution import Solution

def test_three():
    assert Solution().numTrees(3) == 5

def test_one():
    assert Solution().numTrees(1) == 1
