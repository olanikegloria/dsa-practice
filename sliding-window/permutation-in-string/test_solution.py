from solution import Solution

def test_true():
    assert Solution().checkInclusion("ab", "eidbaooo") is True

def test_false():
    assert Solution().checkInclusion("ab", "eidboaoo") is False
