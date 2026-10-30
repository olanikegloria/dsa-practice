# Substring with Concatenation of All Words

**Topic:** sliding-window  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/

## Problem

You are given a string s and an array of strings words. All the strings of words are of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and in any order.

## Approach

Sliding window per offset

## Explanation

Slide window aligned to word length; track word counts.

## Complexity

- Time: O(n * wordLen)
- Space: O(m)

## Alternatives

Hash map of concatenated permutations.

## Common mistakes

Not resetting on unknown word.

## Learning notes

Try each starting offset mod word length.

## Solution

```python
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

```
