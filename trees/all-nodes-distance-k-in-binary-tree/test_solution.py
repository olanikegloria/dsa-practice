from solution import Solution, TreeNode

def build():
    root = TreeNode(3)
    root.left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root.right = TreeNode(1, TreeNode(0), TreeNode(8))
    return root

def test_example():
    root = build()
    target = root.left
    out = sorted(Solution().distanceK(root, target, 2))
    assert out == [1, 4, 7]

def test_self():
    root = TreeNode(1)
    assert Solution().distanceK(root, root, 0) == [1]
