from solution import Solution

def test_example():
    got = {tuple(x) for x in Solution().combinationSum([2,3,6,7], 7)}
    assert got == {(2,2,3), (7,)}

def test_none():
    assert Solution().combinationSum([2], 1) == []
