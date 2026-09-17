from solution import Solution

def test_positive():
    assert Solution().reverseInteger(123) == 321

def test_negative():
    assert Solution().reverseInteger(-123) == -321

def test_overflow():
    assert Solution().reverseInteger(1534236469) == 0
