from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # previous begins as None because the new tail must point to None
        previous = None

        # current is the traversal pointer and begins at the original head
        current = head

        # continues while current refers to a node
        while current:

            # preserves the next node before changing current.next
            next_node = current.next

            # reverses the link so current points to the previous node
            current.next = previous

            # advances both traversal references one node forward
            previous = current
            current = next_node

        # previous now refers to the new head of the reversed list
        return previous

# iterative pointer reversal uses three references:
# previous, current, and next_node.
