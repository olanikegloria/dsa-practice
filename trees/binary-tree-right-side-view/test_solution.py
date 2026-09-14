from solution import Solution, TreeNode

def test_example():
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert Solution().rightSideView(root) == [1, 3, 4]

def test_single():
    assert Solution().rightSideView(TreeNode(1)) == [1]
