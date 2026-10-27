# Roman to Integer

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/roman-to-integer/

## Problem

Given a string s representing a Roman numeral, convert it to an integer.

## Approach

Left-to-right scan

## Explanation

Add symbol value unless a larger symbol follows (subtractive case).

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Right-to-left accumulation.

## Common mistakes

Always adding without subtractive check.

## Learning notes

Compare each char with its right neighbor.

## Solution

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i, ch in enumerate(s):
            if i + 1 < len(s) and values[ch] < values[s[i + 1]]:
                total -= values[ch]
            else:
                total += values[ch]
        return total

```
