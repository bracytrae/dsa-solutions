# Implement a LIFO stack using two FIFO queues.
# Keep the most recently pushed value at the front of the main queue.

from collections import deque

# deque supports O(1) enqueue and dequeue operations at opposite ends

class MyStack:

    def __init__(self):

        # main_queue stores elements in stack order
        """
            main_queue

            front → [ ] ← rear
        """
        self.main_queue = deque()

        # auxiliary_queue temporarily holds elements during push
        self.auxiliary_queue = deque()

    def push(self, x: int) -> None:

        # enqueue the new value first so it becomes the stack's top
        self.auxiliary_queue.append(x)

        # transfer existing values behind the new value
        while self.main_queue:
            self.auxiliary_queue.append(self.main_queue.popleft())

        # swap the queue references; the auxiliary queue becomes empty helper storage
        self.main_queue, self.auxiliary_queue = self.auxiliary_queue, self.main_queue

    def pop(self) -> int:

        # dequeue and return the value representing the stack's top
        return self.main_queue.popleft()

    def top(self) -> int:

        # peek at the stack's top without removing it
        return self.main_queue[0]

    def empty(self) -> bool:

        # the stack is empty exactly when the main queue is empty
        return len(self.main_queue) == 0
