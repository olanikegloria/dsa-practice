# Course Schedule

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/course-schedule/

## Problem

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. Return true if you can finish all courses. Otherwise, return false.

## Approach

Topological sort on an adjacency list

## Explanation

Build the graph of course dependencies, then Kahn-sort. If every course is visited, there is no cycle.

## Complexity

- Time: O(V + E)
- Space: O(V + E)

## Alternatives

DFS with a recursion-stack cycle check.

## Common mistakes

Reversing the edge direction, or treating a leftover indegree as success.

## Learning notes

A cycle in the prerequisite graph is exactly an impossible schedule.

## Solution

```python
from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, need in prerequisites:
            graph[need].append(course)
            indegree[course] += 1
        q = deque(i for i, d in enumerate(indegree) if d == 0)
        seen = 0
        while q:
            cur = q.popleft()
            seen += 1
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return seen == numCourses

```
