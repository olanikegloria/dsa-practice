from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: List[int] = []
        for n in nums:
            lo, hi = 0, len(tails)
            while lo < hi:
                mid = (lo + hi) // 2
                if tails[mid] < n:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == len(tails):
                tails.append(n)
            else:
                tails[lo] = n
        return len(tails)
