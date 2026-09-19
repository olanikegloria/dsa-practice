# Count and Say

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/count-and-say/

## Problem

The count-and-say sequence is a sequence of digit strings defined by the recursive formula. Given a positive integer n, return the nth term of the count-and-say sequence.

## Approach

Simulation

## Explanation

Iteratively build the next term by run-length encoding the previous string.

## Complexity

- Time: O(n * L) where L is max string length
- Space: O(L)

## Alternatives

Recursive generation.

## Common mistakes

Off-by-one on run boundaries.

## Learning notes

Classic run-length encoding drill.

## Solution

```python
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            nxt = []
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                nxt.append(str(j - i))
                nxt.append(s[i])
                i = j
            s = "".join(nxt)
        return s

```
