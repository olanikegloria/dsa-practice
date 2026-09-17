# Reverse Integer

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/reverse-integer/

## Problem

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

## Approach

Digit extraction

## Explanation

Build reversed digits; clamp to 32-bit signed range.

## Complexity

- Time: O(log x)
- Space: O(1)

## Alternatives

Convert to string and reverse.

## Common mistakes

Forgetting overflow check after applying sign.

## Learning notes

Use divmod in a loop for digit reversal.

## Solution

```python
class Solution:
    def reverseInteger(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        rev *= sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev

```
