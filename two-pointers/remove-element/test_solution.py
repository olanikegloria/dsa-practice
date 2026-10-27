from solution import Solution

def test_remove_threes():
    nums = [3, 2, 2, 3]
    assert Solution().removeElement(nums, 3) == 2
    assert nums[:2] == [2, 2]

def test_all_removed():
    nums = [1, 1, 1]
    assert Solution().removeElement(nums, 1) == 0
