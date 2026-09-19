# Evaluate Division

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/evaluate-division/

## Problem

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent Ai / Bi = values[i]. Return the answers to all queries.

## Approach

Graph BFS

## Explanation

Build weighted graph; BFS multiply edge weights along path.

## Complexity

- Time: O(Q * (V + E))
- Space: O(V + E)

## Alternatives

Union-Find with weights.

## Common mistakes

Missing unknown variable check.

## Learning notes

Division queries become path products on a graph.

## Solution

```python
from typing import List
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v

        def bfs(src, dst):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            q = deque([(src, 1.0)])
            seen = {src}
            while q:
                node, cur = q.popleft()
                for nxt, w in graph[node].items():
                    if nxt in seen:
                        continue
                    nval = cur * w
                    if nxt == dst:
                        return nval
                    seen.add(nxt)
                    q.append((nxt, nval))
            return -1.0

        return [bfs(a, b) for a, b in queries]

```
