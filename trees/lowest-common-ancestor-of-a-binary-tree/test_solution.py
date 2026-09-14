from solution import Solution, TreeNode

def test_example():
    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(0), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    p = root.left
    q = root.right
    assert Solution().lowestCommonAncestor(root, p, q).val == 3
