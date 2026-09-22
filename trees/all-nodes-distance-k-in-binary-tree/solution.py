from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def walk(node, par):
            if not node:
                return
            parent[node] = par
            walk(node.left, node)
            walk(node.right, node)

        walk(root, None)
        q = [(target, 0)]
        seen = {target}
        out = []
        idx = 0
        while idx < len(q):
            node, d = q[idx]
            idx += 1
            if d == k:
                out.append(node.val)
            elif d < k:
                for nxt in (node.left, node.right, parent.get(node)):
                    if nxt and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, d + 1))
        return out
