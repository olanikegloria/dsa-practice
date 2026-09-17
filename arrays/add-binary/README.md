# Add Binary

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/add-binary/

## Problem

Given two binary strings a and b, return their sum as a binary string.

## Approach

Two-pointer addition

## Explanation

Add from least significant bit with carry.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

Convert to int then bin().

## Common mistakes

Forgetting final carry digit.

## Learning notes

Same pattern as add-two-numbers on strings.

## Solution

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        out = []
        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0:
                s += int(a[i])
                i -= 1
            if j >= 0:
                s += int(b[j])
                j -= 1
            out.append(str(s % 2))
            carry = s // 2
        return "".join(reversed(out))

```
