from solution import Solution

def test_example():
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"

def test_none():
    assert Solution().minWindow("a", "aa") == ""
