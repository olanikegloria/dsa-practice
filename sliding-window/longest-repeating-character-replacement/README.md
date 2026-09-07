# Longest Repeating Character Replacement

**Topic:** sliding-window  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/longest-repeating-character-replacement/

## Problem

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times. Return the length of the longest substring containing the same letter you can achieve after performing the above operations.

## Approach

Sliding window + frequency

## Explanation

Window is valid if length - most frequent char <= k replacements.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Binary search on length + window check.

## Common mistakes

Forgetting the window shrink condition.

## Learning notes

Max-frequency windows show up in many string DP/window problems.

## Solution

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = best = maxf = 0
        for right, ch in enumerate(s):
            idx = ord(ch) - 65
            count[idx] += 1
            maxf = max(maxf, count[idx])
            while right - left + 1 - maxf > k:
                count[ord(s[left]) - 65] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best

```
