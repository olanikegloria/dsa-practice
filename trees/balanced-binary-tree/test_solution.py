from solution import Solution, TreeNode

def test_balanced():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().isBalanced(root) is True

def test_unbalanced():
    root = TreeNode(1, TreeNode(2, TreeNode(3), None), None)
    assert Solution().isBalanced(root) is False
