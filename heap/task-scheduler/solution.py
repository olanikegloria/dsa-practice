from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        maxf = max(counts)
        ties = counts.count(maxf)
        return max(len(tasks), (maxf - 1) * (n + 1) + ties)
