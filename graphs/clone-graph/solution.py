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
