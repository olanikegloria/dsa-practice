from solution import Solution, Node

def build(pairs):
    nodes = [Node(v) for v, _ in pairs]
    for i, (_, r) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if r is not None:
            nodes[i].random = nodes[r]
    return nodes[0]

def collect(head):
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    return nodes

def test_copy():
    src = build([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    cp = Solution().copyRandomList(src)
    orig = collect(src)
    cloned = collect(cp)
    assert len(orig) == len(cloned)
    for o, c in zip(orig, cloned):
        assert c.val == o.val
        assert c is not o
        if o.random is None:
            assert c.random is None
        else:
            assert cloned[orig.index(o.random)] is c.random
