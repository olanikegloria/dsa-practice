from solution import Solution

def test_example():
    out = sorted(tuple(p) for p in Solution().kClosest([[1,3],[-2,2]], 1))
    assert out == [(-2,2)]

def test_k2():
    out = sorted(tuple(p) for p in Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))
    assert out == sorted([(3,3),(-2,4)])
