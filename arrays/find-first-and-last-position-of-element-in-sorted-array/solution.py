from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bound():
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def right_bound():
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo - 1

        if not nums:
            return [-1, -1]
        l, r = left_bound(), right_bound()
        if l > r or nums[l] != target:
            return [-1, -1]
        return [l, r]
