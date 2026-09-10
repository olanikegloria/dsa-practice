from solution import Solution, TreeNode

def test_example():
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert Solution().kthSmallest(root, 1) == 1
    assert Solution().kthSmallest(root, 3) == 3
