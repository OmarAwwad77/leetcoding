# link: https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

class ListNode:
    def __init__(self, value= 0, _next= None):
        self.value = value
        self.next: ListNode = _next
    def __repr__(self):
        return f"value: {self.value}. next: {self.next}"

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head: return None
    prev = None
    curr = head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev

head = ListNode(0 , ListNode(1, ListNode(2)))
print(reverse_list(head))

