from solution import Solution, TreeNode

def test_true():
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    assert Solution().hasPathSum(root, 22) is True

def test_false():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().hasPathSum(root, 5) is False
