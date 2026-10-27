# Valid Number

**Topic:** arrays  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/valid-number/

## Problem

Given a string s, return whether s is a valid number.

## Approach

Finite scan with flags

## Explanation

Track digits, dot, and exponent; validate char context.

## Complexity

- Time: O(n)
- Space: O(1)

## Alternatives

Regex (harder to get edge cases).

## Common mistakes

Allowing multiple dots or exponent without digits.

## Learning notes

LeetCode number parsing edge cases.

## Solution

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        seen_digit = seen_dot = seen_exp = False
        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True
            elif ch in "+-":
                if i != 0 and s[i - 1] not in "eE":
                    return False
            elif ch == ".":
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            elif ch in "eE":
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False
            else:
                return False
        return seen_digit

```
