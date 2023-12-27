# link: https://leetcode.com/problems/reverse-linked-list-ii/
from typing import Optional

class ListNode:
    def __init__(self, val= 0, _next= None):
        self.val = val
        self.next: ListNode = _next
    def __repr__(self):
        return f"val: {self.val}. next: {self.next}"


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head: return head
    curr = head
    pos = 1
    start = None
    end = None
    prev = None
    node_before_reverse = None

    while curr and pos <= right:
        if left <= pos and pos <= right:
            if left == pos:
                start = curr
            if right == pos:
                end = curr
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        else:
            node_before_reverse = curr
            curr = curr.next
        pos += 1

    start.next = curr
    if node_before_reverse:
        node_before_reverse.next = end
    else:
        head = end
    return head
