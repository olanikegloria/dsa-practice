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

def test_pairs():
    assert to_list(Solution().swapPairs(build([1, 2, 3, 4]))) == [2, 1, 4, 3]

def test_odd():
    assert to_list(Solution().swapPairs(build([1, 2, 3]))) == [2, 1, 3]
