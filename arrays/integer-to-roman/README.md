# Integer to Roman

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/integer-to-roman/

## Problem

Given an integer, convert it to a Roman numeral.

## Approach

Greedy with value-symbol table

## Explanation

Greedy subtract largest Roman value symbols while num remains.

## Complexity

- Time: O(1)
- Space: O(1)

## Alternatives

Hard-coded digit buckets per place.

## Common mistakes

Wrong subtractive pair order.

## Learning notes

Fixed num range makes greedy safe.

## Solution

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        pairs = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
        ]
        out = []
        for val, sym in pairs:
            while num >= val:
                out.append(sym)
                num -= val
        return "".join(out)

```
