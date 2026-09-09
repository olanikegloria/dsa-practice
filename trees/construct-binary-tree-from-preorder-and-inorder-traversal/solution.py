from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {v: i for i, v in enumerate(inorder)}
        i = 0

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            nonlocal i
            if lo > hi:
                return None
            val = preorder[i]
            i += 1
            mid = index[val]
            node = TreeNode(val)
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(inorder) - 1)
