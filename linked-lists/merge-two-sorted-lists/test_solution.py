from solution import Solution, ListNode

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def test_merge():
    a = ListNode(1, ListNode(2, ListNode(4)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    assert to_list(Solution().mergeTwoLists(a, b)) == [1,1,2,3,4,4]
