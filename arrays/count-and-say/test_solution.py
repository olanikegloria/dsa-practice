from solution import Solution

def test_four():
    assert Solution().countAndSay(4) == "1211"

def test_one():
    assert Solution().countAndSay(1) == "1"
