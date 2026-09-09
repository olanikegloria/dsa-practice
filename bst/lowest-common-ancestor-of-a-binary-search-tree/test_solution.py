from solution import Solution, TreeNode

def test_split():
    n2, n4 = TreeNode(2), TreeNode(4)
    n3 = TreeNode(3, n2, n4)
    n7, n9 = TreeNode(7), TreeNode(9)
    n8 = TreeNode(8, n7, n9)
    root = TreeNode(6, n3, n8)
    assert Solution().lowestCommonAncestor(root, n2, n8) is root

def test_ancestor_is_target():
    n2, n4 = TreeNode(2), TreeNode(4)
    n3 = TreeNode(3, n2, n4)
    assert Solution().lowestCommonAncestor(n3, n2, n3) is n3
