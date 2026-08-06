from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # a reverse linked list needs a real ending 

        # no node comes before the head initially
        previous = None

        # start's at the first node which is the head
        current = head

        # continue's as long as the head/current points to a node
        while current:

            # next_node points to the next node after current
            next_node = current.next

            # make's the current node point to the previous node
            current.next = previous

            # points to the current node
            previous = current

            # points the current node to the saved next node
            current = next_node

        # return's the new head for the reversed list
        return previous

# structure of val.next --> [ val: [...] | next: [Node] ] 

# to change a particular node you need a variable that points to that node 

# keeping track of previous lets you know where you are within the linked list 
