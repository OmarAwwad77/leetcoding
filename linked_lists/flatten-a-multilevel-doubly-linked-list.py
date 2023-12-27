# link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
from typing import Optional, List, Any

class Node:
    def __init__(self, val, prev, _next, child):
        self.val = val
        self.prev = prev
        self.next = _next
        self.child = child

# stack
def flatten(head: Optional[Node]) -> Optional[Node]:
    if not head: return head
    stack: List[Node] = [head]
    while stack:
        curr = stack.pop()
        if curr.next:
            stack.append(curr.next)
        if curr.child:
            stack.append(curr.child)
            curr.child = None
        if stack:
            next_node = stack[-1]
            curr.next = next_node
            next_node.prev = curr
    return head


# recursion
def get_tail(head: Node) -> Node:
    curr = head
    prev = head
    while curr:
        if curr.child:
            tail = get_tail(curr.child)
            next_node = curr.next
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
            tail.next = next_node
            if next_node:
                next_node.prev = tail
        prev = curr
        curr = curr.next
    return prev


def flatten(head: 'Optional[Node]') -> Optional[Node]:
    if not head: return head
    curr = head

    while curr:
        if curr.child:
            tail = get_tail(curr.child)
            next_node = curr.next
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
            tail.next = next_node
            if next_node:
                next_node.prev = tail
            curr = next_node
            continue
        curr = curr.next
    return head
