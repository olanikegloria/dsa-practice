from solution import Solution

def test_example():
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

def test_none():
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
