# queue implementation using a linked list

# creates each student so each student becomes a node in the queue

# so this creates individual students/nodes

"""
    each student becomes a node

    val stores the student's sandwich preference 

    next points to the next student in the queue 

                ↓

    [val: 1 | next: [Node]]
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# the queue controls the linked list controlling the front and rear nodes
class Queue:

    """
        initially there are no students 

        front = None 
        rear = None 
        size = 0

        the queue needs both front and rear because 

        dequeue → remove's from front
        enqueue → add's to rear
    """

    # this is the contructor for the queue, it initializes the front and rear to None and size to 0
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

    # adds a student to the rear of the queue
    # this is what builds and preserves the linked-list-queue
    def enqueue(self, val):

        new_node = ListNode(val)

        # when the queue is empty which inevitably happens at the start, the front and rear both point to the new node

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

            # rear points to the new node
            """
                front
                ↓
                [1] -> [2] -> None
                        ↑
                    rear
            """

            self.rear.next = new_node

            # rear points to the new last node
            """
                front
                ↓
                [1] -> [2] -> None
                                ↑
                            rear
            """

            self.rear = new_node

        # increments the size of the queue
        self.size += 1

    def dequeue(self):

        # checks if the queue is empty, if it is then it returns None
        if self.front is None:
            return None

        # save's the value of the front of the node
        val = self.front.val

        # front points to the next node that will be saved in the queue
        self.front = self.front.next

        # decrements the size of the queue
        self.size -= 1

        # if the front is empty then the queue becomes empty
        if self.front is None:
            self.rear = None

        # returns the value of the front node that was removed from the queue
        return val

# uses the Queue class to simulate the cafeteria problem
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:

        # creates the empty queue for the students
        queue = Queue()

        # add every student to the queue
        for student in students:
            queue.enqueue(student)

            """
            queue.enqueue(1)
            queue.enqueue(0)
            etc...
            """

        # starts at index 0 of the sandwiches list 
        sandwich = 0

       # number of students who rejected the current sandwich 
        skipped = 0

        # continues as long as there are students in the queue so while the queue is not empty
        while queue.size > 0:

            # if the student at the front of the queue wants the current sandwich
            if queue.front.val == sandwiches[sandwich]:

                # remove's student from front
                queue.dequeue()

                # points to the next sandwich
                sandwich += 1

                # moves on to the new sandwich, so skipped is reset
                skipped = 0

            # if the student at the front of the queue does not want the current sandwich
            else:

                # remove's student from front
                student = queue.dequeue()

                # add the student back to the rear
                queue.enqueue(student)

                # increments the number of students who have rejected the current sandwich
                skipped += 1

                # if all students in the queue have rejected the current sandwich then the loop breaks and the number of students left in the queue is returned
                if skipped == queue.size:
                    break

        return queue.size