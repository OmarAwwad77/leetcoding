import math
from functools import partial
from typing import Optional


class PriorityQueue:
    def __init__(self, comparator=partial(lambda a, b: a > b)):
        self._comparator = comparator
        self._heap = []

    def size(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return bool(self._heap)

    def peak(self) -> int:
        return self._heap[0]

    def push(self, num: int):
        self._heap.append(num)
        self._shift_up()

    def pop(self) -> Optional[int]:
        if not self._heap:
            return
        head = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        self._shift_down()
        return head

    def _shift_down(self, idx=0):
        left_idx = self._get_child_idx(idx)
        right_idx = self._get_child_idx(idx, False)
        indices_to_compare = [idx for idx in (left_idx, right_idx) if idx is not None]

        while indices_to_compare:
            curr_idx = idx
            if len(indices_to_compare) == 1:
                if self._comparator(self._heap[indices_to_compare[0]], self._heap[idx]):
                    self._swap(indices_to_compare[0], idx)
                    idx = indices_to_compare[0]
            else: # 2
                if self._comparator(self._heap[indices_to_compare[0]], self._heap[indices_to_compare[1]]):
                    if self._comparator(self._heap[indices_to_compare[0]], self._heap[idx]):
                        self._swap(indices_to_compare[0], idx)
                        idx = indices_to_compare[0]
                else:
                    if self._comparator(self._heap[indices_to_compare[1]], self._heap[idx]):
                        self._swap(indices_to_compare[1], idx)
                        idx = indices_to_compare[1]

            if curr_idx == idx:
                return
            left_idx = self._get_child_idx(idx)
            right_idx = self._get_child_idx(idx, False)
            indices_to_compare = [idx for idx in (left_idx, right_idx) if idx is not None]

    def _shift_up(self):
        idx = self.size() - 1
        parent_idx = self._get_parent_idx(idx)
        while parent_idx is not None and self._comparator(self._heap[idx],  self._heap[parent_idx]):
            self._swap(idx, parent_idx)
            idx = parent_idx
            parent_idx = self._get_parent_idx(idx)

    def _swap(self, a: int, b: int):
        tmp = self._heap[a]
        self._heap[a] = self._heap[b]
        self._heap[b] = tmp

    def _get_child_idx(self, idx: int, left=True) -> Optional[int]:
        child_idx = idx * 2 + 1 if left else idx * 2 + 2
        return child_idx if child_idx < self.size() else None

    @staticmethod
    def _get_parent_idx(idx: int) -> Optional[int]:
        parent_idx = math.floor((idx - 1) / 2)
        return parent_idx if parent_idx >= 0 else None


priority_queue = PriorityQueue()
priority_queue.push(20)
priority_queue.push(45)
priority_queue.push(40)
priority_queue.push(35)
priority_queue.push(10)
priority_queue.push(15)
priority_queue.push(25)
priority_queue.push(50)
priority_queue.push(75)

print(priority_queue._heap)
print(priority_queue.pop())
print(priority_queue.pop())
print(priority_queue.pop())
print(priority_queue.pop())
print(priority_queue.pop())
print(priority_queue.pop())
print(priority_queue.pop())
print(priority_queue.pop())
print(priority_queue.pop())
print(priority_queue.pop())

