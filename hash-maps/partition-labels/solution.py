from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        start = 0
        end = 0
        parts = []
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                parts.append(end - start + 1)
                start = i + 1
        return parts
