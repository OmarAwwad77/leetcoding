# link: https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        self.stack = []
        self.stack_reversed = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack_reversed:
            self._populate_reversed()
        return self.stack_reversed.pop()

    def peek(self) -> int:
        if not self.stack_reversed:
            self._populate_reversed()
        return self.stack_reversed[-1]

    def empty(self) -> bool:
        if not self.stack and not self.stack_reversed:
            return True
        return False

    def _populate_reversed(self):
        for i in range(len(self.stack)):
            self.stack_reversed.append(self.stack.pop())