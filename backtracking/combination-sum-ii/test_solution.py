from solution import Solution

def test_example():
    out = sorted(tuple(c) for c in Solution().combinationSum2([10,1,2,7,6,1,5], 8))
    assert out == sorted([(1,1,6),(1,2,5),(1,7),(2,6)])
