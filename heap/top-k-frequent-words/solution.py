from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = [(-counts[w], w) for w in counts]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
