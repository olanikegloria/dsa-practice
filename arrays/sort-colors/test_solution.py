from solution import Solution

def test_example():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
