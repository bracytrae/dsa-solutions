# Linked-list implementation of a FIFO queue.

"""
    each student is stored in a node

    val stores the student's sandwich preference

    next stores a reference to the next node in the queue

                ↓

    [val: 1 | next: [Node]]
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# front supports dequeue, and rear supports O(1) enqueue
class Queue:

    """
        initially there are no students

        front = None
        rear = None
        size = 0

        dequeue → remove from the front
        enqueue → insert at the rear
    """

    # initializes an empty queue
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    """
        front                    rear
        ↓                        ↓
        [1] -> [0] -> [1] -> [0] -> None

        size = 4
    """

    # enqueues a value at the rear of the queue
    def enqueue(self, val):

        new_node = ListNode(val)

        # in a one-node queue, front and rear refer to the same node

        """
            ex.

            enqueue(10)

            front
            ↓
            [10]
            ↑
            rear
        """

        if self.front is None:
            self.front = new_node
            self.rear = new_node

        else:

            # links the old rear node to the new node
            """
                front
                ↓
                [1] -> [2] -> None
                        ↑
                    rear
            """

            self.rear.next = new_node

            # updates rear to the new final node
            """
                front
                ↓
                [1] -> [2] -> None
                                ↑
                            rear
            """

            self.rear = new_node

        # increments the number of nodes in the queue
        self.size += 1

    def dequeue(self):

        # handles queue underflow by returning None
        if self.front is None:
            return None

        # preserves the front value before unlinking its node
        val = self.front.val

        # dequeues the front node by advancing the front reference
        self.front = self.front.next

        # decrements the number of nodes in the queue
        self.size -= 1

        # restores the empty-queue invariant: both front and rear are None
        if self.front is None:
            self.rear = None

        # returns the dequeued value
        return val

# simulates the cafeteria process with the linked-list queue
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:

        # initialize the student queue
        queue = Queue()

        # enqueues students in their original order
        for student in students:
            queue.enqueue(student)

            """
            queue.enqueue(1)
            queue.enqueue(0)
            etc...
            """

        # tracks the index of the sandwich at the top of the stack
        sandwich_index = 0

        # counts consecutive rejections of the current sandwich
        skipped = 0

        # processes students until the queue is empty or no student accepts the top sandwich
        while queue.size > 0:

            # if the student at the front of the queue wants the current sandwich
            if queue.front.val == sandwiches[sandwich_index]:

                # dequeues the student who accepts the sandwich
                queue.dequeue()

                # advances the top of the sandwich stack
                sandwich_index += 1

                # resets the rejection count for the new top sandwich
                skipped = 0

            # if the student at the front of the queue does not want the current sandwich
            else:

                # dequeues the student who rejected the sandwich
                student = queue.dequeue()

                # enqueues that student at the rear
                queue.enqueue(student)

                # counts this consecutive rejection
                skipped += 1

                # stops processing after one full queue rotation without a matching sandwich preference
                if skipped == queue.size:
                    break

        return queue.size
