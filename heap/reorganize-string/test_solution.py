from solution import Solution

def test_aab():
    assert Solution().reorganizeString("aab") == "aba"

def test_impossible():
    assert Solution().reorganizeString("aaab") == ""
