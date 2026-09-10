from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for value, frequency in counts.items():
            buckets[frequency].append(value)
        out: List[int] = []
        for frequency in range(len(buckets) - 1, 0, -1):
            for value in buckets[frequency]:
                out.append(value)
                if len(out) == k:
                    return out
        return out
