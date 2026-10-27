# Plus One

**Topic:** arrays  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/plus-one/

## Problem

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. Increment the large integer by one and return the resulting array of digits.

## Approach

Single pass from end

## Explanation

Propagate carry from the right; prepend 1 if all nines.

## Complexity

- Time: O(n)
- Space: O(1) excluding output

## Alternatives

Convert to int (may overflow).

## Common mistakes

Not handling all-nines case.

## Learning notes

Classic carry propagation.

## Solution

```python
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

```
