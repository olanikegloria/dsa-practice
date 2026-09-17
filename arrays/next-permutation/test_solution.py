from solution import Solution

def test_increase():
    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    assert nums == [1, 3, 2]

def test_descending():
    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    assert nums == [1, 2, 3]
