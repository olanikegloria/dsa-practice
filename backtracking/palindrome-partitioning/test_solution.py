from solution import Solution

def test_example():
    got = {tuple(p) for p in Solution().partition("aab")}
    assert got == {("a", "a", "b"), ("aa", "b")}
