from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
each node contains

[val | next]

this solution reverses the links in a singly linked list using recursion
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # base case: an empty list or one-node list is already reversed
        # the original tail becomes the head during recursion unwinding
        if head is None or head.next is None:
            return head

        # recursively reverses the sublist beginning at head.next
        new_head = self.reverseList(head.next)

        # during recursion unwinding, this reverses the link back to the current node
        head.next.next = head

        # breaks the old forward link; the original head becomes the new tail
        head.next = None

        # propagates the new head back through the recursive call stack
        return new_head
