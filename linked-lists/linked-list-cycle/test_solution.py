from solution import Solution, ListNode

def test_cycle():
    a = ListNode(3); b = ListNode(2); c = ListNode(0)
    a.next = b; b.next = c; c.next = b
    assert Solution().hasCycle(a) is True

def test_no_cycle():
    a = ListNode(1); a.next = ListNode(2)
    assert Solution().hasCycle(a) is False
