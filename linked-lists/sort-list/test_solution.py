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

def test_sort():
    assert to_list(Solution().sortList(ll([4, 2, 1, 3]))) == [1, 2, 3, 4]
