from solution import Solution

def test_found():
    assert Solution().strStr("sadbutsad", "sad") == 0

def test_missing():
    assert Solution().strStr("leetcode", "leeto") == -1
