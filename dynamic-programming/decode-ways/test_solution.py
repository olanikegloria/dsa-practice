from solution import Solution

def test_example():
    assert Solution().numDecodings("12") == 2

def test_zero():
    assert Solution().numDecodings("06") == 0
