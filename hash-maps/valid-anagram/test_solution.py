from solution import Solution

def test_true():
    assert Solution().isAnagram("anagram", "nagaram") is True

def test_false():
    assert Solution().isAnagram("rat", "car") is False
