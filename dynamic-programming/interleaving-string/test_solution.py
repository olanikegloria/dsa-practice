from solution import Solution

def test_true():
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") is True

def test_false():
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
