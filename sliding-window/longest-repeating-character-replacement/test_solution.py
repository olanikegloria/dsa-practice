from solution import Solution

def test_example():
    assert Solution().characterReplacement("ABAB", 2) == 4

def test_aab():
    assert Solution().characterReplacement("AABABBA", 1) == 4
