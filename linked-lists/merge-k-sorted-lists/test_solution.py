from solution import Solution, ListNode

def ll(v):
    d = ListNode(0)
    c = d
    for x in v:
        c.next = ListNode(x)
        c = c.next
    return d.next

def to(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def test_example():
    lists = [ll([1, 4, 5]), ll([1, 3, 4]), ll([2, 6])]
    assert to(Solution().mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
