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
    assert to(Solution().addTwoNumbers(ll([2, 4, 3]), ll([5, 6, 4]))) == [7, 0, 8]
