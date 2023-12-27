# link: https://leetcode.com/problems/linked-list-cycle-ii/
from typing import Optional

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

# brute-force Time: O(n), Space: O(n)
def detect_cycle(head: Optional[Node]) -> Optional[Node]:
    if not head: return None
    seen = set()
    curr = head

    while curr:
        if curr in seen:
            return curr
        seen.add(curr)
        curr = curr.next

    return None


# optimal (Floyd's tortoise and hare algorithm) Time: O(n), Space: O(n)
def detect_cycle(head: Optional[Node]) -> Optional[Node]:
    if not head: return None
    curr = None
    tortoise = head.next
    hare = tortoise.next if tortoise else None

    while hare:
        if tortoise == curr:
            return curr
        if hare == tortoise and not curr:
            curr = head
            continue
        tortoise = tortoise.next
        hare = hare.next.next if hare.next else None
        curr = curr.next if curr else None
    return None


# more verbose implementation of Floyd's tortoise and hare algorithm
def detect_cycle(head: Optional[Node]) -> Optional[Node]:
    if not head: return None
    curr = head
    tortoise = head.next
    hare = tortoise.next if tortoise else None
    cycle_detected = False

    while hare:
        if cycle_detected:
            if tortoise == curr:
                return curr
            tortoise = tortoise.next
            curr = curr.next
            continue
        if hare == tortoise:
            cycle_detected = True
            continue
        tortoise = tortoise.next
        hare = hare.next.next if hare.next else None
    return None