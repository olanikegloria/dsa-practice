from solution import Solution, ListNode

def build(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def test_k2():
    assert to_list(Solution().reverseKGroup(build([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]

def test_k3():
    assert to_list(Solution().reverseKGroup(build([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
