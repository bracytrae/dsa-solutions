# stack implementation using two queues

# make's a fifo structure behave like a lifo structure 
# there are two fifo queues but we arrange them so the newest value is always at the front of the main queue which makes the queues behave like a lifo stack

from collections import deque

# deque is a python container that can behave like a queue

class MyStack:

    def __init__(self):

        # main queue
        """
            q1

            front → [ ] ← rear      
        """
        self.q1 = deque()

        # temporary queue used to rearrange elements
        self.q2 = deque()

    def push(self, x: int) -> None:

        # adds the newest value to the empty temporary queue
        self.q2.append(x)

        # move's everything from q1 to q2 so the newest value is at the front of q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # q2 now has the stack order we want so q2 becomes the main queue and q1 becomes the temporary queue for the next push
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:

        # removes the value at the front of q1 and returns the removed value 
        return self.q1.popleft()

    def top(self) -> int:

        # returns the value at the front of q1 without removing it
        return self.q1[0]

    def empty(self) -> bool:

        # returns True if the main queue which is q1 is empty and False if it is not
        return len(self.q1) == 0
        