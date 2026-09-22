# Open the Lock

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/open-the-lock/

## Problem

You have a lock with four circular wheels, each wheel has 10 slots labeled "0" to "9". Given deadends and a target, return the minimum turns to open the lock starting from "0000", or -1 if impossible.

## Approach

BFS on state space

## Explanation

BFS from 0000 over wheel turns, skipping deadends.

## Complexity

- Time: O(10^4)
- Space: O(10^4)

## Alternatives

Bidirectional BFS.

## Common mistakes

Not blocking start in deadends.

## Learning notes

Each dial has two neighbors mod 10.

## Solution

```python
from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        q = deque([("0000", 0)])
        seen = {"0000"}
        while q:
            state, turns = q.popleft()
            if state == target:
                return turns
            for i in range(4):
                digit = int(state[i])
                for d in (-1, 1):
                    nd = (digit + d) % 10
                    nxt = state[:i] + str(nd) + state[i + 1 :]
                    if nxt not in seen and nxt not in dead:
                        seen.add(nxt)
                        q.append((nxt, turns + 1))
        return -1

```
