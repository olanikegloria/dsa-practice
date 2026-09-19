from solution import Solution

def test_example():
    eq = [["a", "b"], ["b", "c"]]
    val = [2.0, 3.0]
    q = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    out = Solution().calcEquation(eq, val, q)
    assert abs(out[0] - 6.0) < 1e-5
    assert abs(out[1] - 0.5) < 1e-5
    assert out[2] == -1.0
    assert abs(out[3] - 1.0) < 1e-5
    assert out[4] == -1.0
