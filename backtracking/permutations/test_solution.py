from solution import Solution

def test_example():
    out = sorted(tuple(p) for p in Solution().permute([1, 2, 3]))
    expected = sorted([(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)])
    assert out == expected
