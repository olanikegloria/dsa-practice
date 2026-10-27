from solution import Solution

def test_123():
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]

def test_nines():
    assert Solution().plusOne([9]) == [1, 0]
