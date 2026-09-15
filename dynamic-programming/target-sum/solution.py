from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for n in nums:
            nxt = defaultdict(int)
            for s, cnt in dp.items():
                nxt[s + n] += cnt
                nxt[s - n] += cnt
            dp = nxt
        return dp.get(target, 0)
