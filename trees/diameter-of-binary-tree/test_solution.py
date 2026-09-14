from solution import Solution, TreeNode

def test_example():
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert Solution().diameterOfBinaryTree(root) == 3
