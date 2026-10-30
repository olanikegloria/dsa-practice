from solution import Solution

def test_barfoo():
    assert Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]

def test_no_match():
    assert Solution().findSubstring("aaaa", ["aa", "aa"]) == [0]
