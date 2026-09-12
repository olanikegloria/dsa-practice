# Happy Number

**Topic:** hash-maps  
**Difficulty:** easy  
**LeetCode:** https://leetcode.com/problems/happy-number/

## Problem

Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

## Approach

Cycle detection with set

## Explanation

Detect cycle in digit-square iteration.

## Complexity

- Time: O(log n) per step
- Space: O(log n)

## Alternatives

Floyd tortoise-hare.

## Common mistakes

Infinite loop without cycle detection.

## Learning notes

Happy numbers always reach 1 or cycle at 4.

## Solution

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(x):
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            n = next_num(n)
        return n == 1

```
