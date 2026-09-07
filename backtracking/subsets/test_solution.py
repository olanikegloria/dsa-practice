from solution import Solution

def test_example():
    got = Solution().subsets([1, 2, 3])
    normalized = {tuple(sorted(x)) for x in got}
    assert normalized == {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}
