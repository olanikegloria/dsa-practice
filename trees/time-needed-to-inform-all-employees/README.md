# Time Needed to Inform All Employees

**Topic:** trees  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/time-needed-to-inform-all-employees/

## Problem

A company has n employees with a unique ID from 0 to n - 1 and a headID. Each employee has a manager and an informTime. Return the number of minutes needed to inform all employees.

## Approach

Tree DFS

## Explanation

Build adjacency from manager array; DFS max subtree inform time.

## Complexity

- Time: O(n)
- Space: O(n)

## Alternatives

BFS level accumulation.

## Common mistakes

Adding inform time at leaves.

## Learning notes

Head inform time applies before children start.

## Solution

```python
from typing import List
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for i, boss in enumerate(manager):
            if boss != -1:
                children[boss].append(i)

        def dfs(u: int) -> int:
            if not children[u]:
                return 0
            return informTime[u] + max(dfs(v) for v in children[u])

        return dfs(headID)

```
