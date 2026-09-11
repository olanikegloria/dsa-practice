from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float("-inf")
        removed = 0
        for start, e in intervals:
            if start < end:
                removed += 1
            else:
                end = e
        return removed
