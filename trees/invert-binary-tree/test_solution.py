from solution import Solution, TreeNode

def test_invert():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    out = Solution().invertTree(root)
    assert out.left.val == 3 and out.right.val == 1
