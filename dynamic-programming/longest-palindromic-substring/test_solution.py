from solution import Solution

def test_example():
    out = Solution().longestPalindrome("babad")
    assert out in ("bab", "aba")

def test_single():
    assert Solution().longestPalindrome("a") == "a"
