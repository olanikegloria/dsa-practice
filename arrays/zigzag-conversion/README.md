# Zigzag Conversion

**Topic:** arrays  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/zigzag-conversion/

## Problem

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows. Read the pattern line by line and return the converted string.

## Approach

Simulation

## Explanation

Simulate writing characters row by row with bouncing direction.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

Math formula for index mapping.

## Common mistakes

Forgetting numRows == 1 edge case.

## Learning notes

Row buffers simplify zigzag simulation.

## Solution

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        row, step = 0, 1
        for ch in s:
            rows[row] += ch
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return "".join(rows)

```
