from solution import Solution

def test_example():
    root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert root.val == 3 and root.left.val == 9
    assert root.right.val == 20 and root.right.left.val == 15 and root.right.right.val == 7
