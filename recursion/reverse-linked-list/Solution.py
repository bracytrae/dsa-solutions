from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
each node contains 

[val | next]

this Solution reverses the pointers within the linked list using recursion 
"""



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # base case
        # determines when the recursive function stop's calling itself

        # if the list is empty or if the list is at the last node it returns the head of the reversed list 
        if head is None or head.next is None:
            return head

        # this makes the next node the new head of the reversed list
        new_head = self.reverseList(head.next)

        # this accesses the next node's pointer and points it back to the current head/node
        head.next.next = head

        # this sets the current head's pointer to None so it doesn't point to the next node anymore
        # this helps create a proper reversed linked list
        head.next = None

        # returns the new head of the reversed list
        return new_head