from solution import Solution

def test_example():
    assert Solution().wordBreak("leetcode", ["leet", "code"]) is True

def test_false():
    assert Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
