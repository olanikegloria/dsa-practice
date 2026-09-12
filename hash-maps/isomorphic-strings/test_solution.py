from solution import Solution

def test_true():
    assert Solution().isIsomorphic("egg", "add") is True

def test_false():
    assert Solution().isIsomorphic("foo", "bar") is False
