from solution import Solution, TreeNode

def test_example():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().maxPathSum(root) == 6

def test_negative():
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().maxPathSum(root) == 42
