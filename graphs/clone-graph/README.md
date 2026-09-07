# Clone Graph

**Topic:** graphs  
**Difficulty:** medium  
**LeetCode:** https://leetcode.com/problems/clone-graph/

## Problem

Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

## Approach

DFS with hashmap

## Explanation

DFS copy each node once; map original → clone to wire neighbors.

## Complexity

- Time: O(V + E)
- Space: O(V)

## Alternatives

BFS queue clone.

## Common mistakes

Creating a new clone on every visit (infinite loop).

## Learning notes

Graph clone is visited-set + reconstruct edges.

## Solution

```python
from typing import Optional

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {}

        def dfs(cur: Node) -> Node:
            if cur in clones:
                return clones[cur]
            copy = Node(cur.val)
            clones[cur] = copy
            copy.neighbors = [dfs(n) for n in cur.neighbors]
            return copy

        return dfs(node)

```
