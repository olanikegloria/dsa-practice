from solution import Solution

def test_example():
    assert Solution().longestCommonSubsequence("abcde", "ace") == 3

def test_none():
    assert Solution().longestCommonSubsequence("abc", "def") == 0
