# Decode Ways

**Topic:** dynamic-programming  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/decode-ways/

## Problem

A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26". Given a string s containing only digits, return the number of ways to decode it.

## Approach

Rolling Fibonacci-style DP

## Explanation

A digit can continue a one-digit letter, and with the previous digit it can form a two-digit letter when the pair is 10 to 26.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

An explicit dp array of size n + 1.

## Common mistakes

Treating a leading zero as valid, or accepting 27 as a letter.

## Learning notes

Zeros only survive as the second digit of 10 or 20.

## Solution

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        prev2, prev1 = 1, 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] != "0":
                cur += prev1
            two = int(s[i - 1:i + 1])
            if 10 <= two <= 26:
                cur += prev2
            prev2, prev1 = prev1, cur
        return prev1

```
