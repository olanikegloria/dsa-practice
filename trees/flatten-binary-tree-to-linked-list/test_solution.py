from solution import Solution, TreeNode

def to_list(root):
    out = []
    while root:
        out.append(root.val)
        assert root.left is None
        root = root.right
    return out

def test_example():
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    Solution().flatten(root)
    assert to_list(root) == [1,2,3,4,5,6]
