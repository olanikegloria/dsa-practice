from solution import Solution, TreeNode

def test_valid():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert Solution().isValidBST(root) is True

def test_invalid():
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert Solution().isValidBST(root) is False
