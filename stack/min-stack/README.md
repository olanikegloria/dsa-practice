# Min Stack

**Topic:** stack  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/min-stack/

## Problem

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

## Approach

Second stack of running minimums

## Explanation

A parallel stack stores the minimum as of each push, so the minimum is always the top of that second stack.

## Complexity

- Time: O(1) per operation
- Space: O(n)

## Alternatives

Store pairs of value and current minimum in one stack.

## Common mistakes

Scanning the stack inside getMin, which makes it O(n).

## Learning notes

Constant time queries usually mean the answer was cached on the way in.

## Solution

```python
class MinStack:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.mins: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins.append(val if not self.mins else min(val, self.mins[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


class Solution:
    def build(self) -> MinStack:
        return MinStack()

```
