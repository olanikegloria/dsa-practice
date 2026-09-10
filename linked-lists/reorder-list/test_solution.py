from solution import Solution, ListNode

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def test_even():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    Solution().reorderList(head)
    assert to_list(head) == [1, 4, 2, 3]
