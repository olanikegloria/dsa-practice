# Word Ladder

**Topic:** graphs  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/word-ladder/

## Problem

A transformation sequence from beginWord to endWord is a sequence where only one letter differs at a time and each intermediate word is in wordList. Return the length of the shortest transformation sequence, or 0 if none exists.

## Approach

BFS

## Explanation

BFS on word graph; remove visited words to avoid cycles.

## Complexity

- Time: O(n * L * 26)
- Space: O(n)

## Alternatives

Bidirectional BFS.

## Common mistakes

Not checking endWord in dictionary.

## Learning notes

Each edge changes one letter.

## Solution

```python
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

```
