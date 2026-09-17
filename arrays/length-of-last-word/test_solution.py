from solution import Solution

def test_simple():
    assert Solution().lengthOfLastWord("Hello World") == 5

def test_trailing():
    assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
