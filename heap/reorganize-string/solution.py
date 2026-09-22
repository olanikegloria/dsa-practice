from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [(-c, ch) for ch, c in counts.items()]
        heapq.heapify(heap)
        prev = None
        out = []
        while heap:
            c, ch = heapq.heappop(heap)
            out.append(ch)
            if prev:
                heapq.heappush(heap, prev)
            prev = (c + 1, ch) if c + 1 else None
        return "" if len(out) != len(s) else "".join(out)
