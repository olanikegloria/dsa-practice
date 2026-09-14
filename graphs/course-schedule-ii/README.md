# Course Schedule II

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/course-schedule-ii/

## Problem

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

## Approach

BFS topological sort

## Explanation

Kahn topological sort; empty if cycle exists.

## Complexity

- Time: O(V+E)
- Space: O(V+E)

## Alternatives

DFS postorder reverse.

## Common mistakes

Not detecting incomplete sort.

## Learning notes

Course order is topological ordering of DAG.

## Solution

```python
from typing import List
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nxt in graph[node]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return order if len(order) == numCourses else []

```
