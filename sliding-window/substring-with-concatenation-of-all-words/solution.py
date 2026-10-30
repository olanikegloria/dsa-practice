from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        wlen = len(words[0])
        total = len(words) * wlen
        need = Counter(words)
        out = []
        for offset in range(wlen):
            left = offset
            counts = Counter()
            used = 0
            for right in range(offset, len(s), wlen):
                word = s[right : right + wlen]
                if word not in need:
                    counts.clear()
                    used = 0
                    left = right + wlen
                    continue
                counts[word] += 1
                used += 1
                while counts[word] > need[word]:
                    drop = s[left : left + wlen]
                    counts[drop] -= 1
                    used -= 1
                    left += wlen
                if used == len(words):
                    out.append(left)
        return out
