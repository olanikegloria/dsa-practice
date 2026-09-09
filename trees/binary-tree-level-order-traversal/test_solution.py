from solution import Solution, TreeNode

def test_example():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]

def test_empty():
    assert Solution().levelOrder(None) == []
