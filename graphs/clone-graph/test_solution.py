from solution import Solution, Node

def test_cycle():
    a, b = Node(1), Node(2)
    a.neighbors = [b]
    b.neighbors = [a]
    c = Solution().cloneGraph(a)
    assert c is not a and c.val == 1
    assert c.neighbors[0].val == 2
    assert c.neighbors[0].neighbors[0] is c
