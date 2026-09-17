from solution import Solution

def test_true():
    assert Solution().isPalindrome(121) is True

def test_false_sign():
    assert Solution().isPalindrome(-121) is False

def test_even():
    assert Solution().isPalindrome(1221) is True
