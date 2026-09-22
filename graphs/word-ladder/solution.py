from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        q = deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + c + word[i + 1 :]
                    if nxt in words:
                        words.remove(nxt)
                        q.append((nxt, steps + 1))
        return 0
