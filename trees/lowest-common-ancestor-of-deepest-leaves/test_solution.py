from solution import Solution, TreeNode

def test_example():
    root = TreeNode(3)
    root.left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root.right = TreeNode(1, TreeNode(0), TreeNode(8))
    lca = Solution().lcaDeepestLeaves(root)
    assert lca.val == 2

def test_single():
    root = TreeNode(1)
    assert Solution().lcaDeepestLeaves(root) is root
