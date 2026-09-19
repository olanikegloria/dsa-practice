# Basic Calculator

**Topic:** stack  
**Difficulty:** hard  
**LeetCode:** https://leetcode.com/problems/basic-calculator/

## Problem

Given a string s representing a valid expression, implement a basic calculator to evaluate it and return the value of the expression.

## Approach

Stack + sign accumulator

## Explanation

Stack stores prior result and sign when entering parentheses.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

Recursive descent parser.

## Common mistakes

Forgetting to flush num at closing paren.

## Learning notes

Sign flipping pattern extends to nested expressions.

## Solution

```python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        res = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-":
                res += sign * num
                num = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                num = 0
            elif ch == ")":
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        return res + sign * num

```
