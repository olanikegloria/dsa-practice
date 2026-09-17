from solution import Solution

def test_short():
    assert Solution().addBinary("11", "1") == "100"

def test_longer():
    assert Solution().addBinary("1010", "1011") == "10101"
