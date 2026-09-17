from solution import Solution, ListNode

def ll(vals):
    d = ListNode(0)
    c = d
    for v in vals:
        c.next = ListNode(v)
        c = c.next
    return d.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def test_rotate():
    assert to_list(Solution().rotateRight(ll([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3]
