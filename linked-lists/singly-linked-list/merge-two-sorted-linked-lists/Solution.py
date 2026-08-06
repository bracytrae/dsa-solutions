from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # this function receives two heads list1 and list2 

        # the temporary starting node is ListNode()
        starting_node = ListNode()

        """
        
        starting_node ─┐
                        ──> [temporary node] ──> None
        current ───────┘
        
        """

        # current initially points to the temporary node, because of the starting_node
        current = starting_node

        # continue's as long as both heads list1 and list2 point to a node
        while list1 and list2:

            # compare's the values of the current nodes of list1 and list2
            if list1.val <= list2.val:

                """

                 initially current point to starting_node, so this connects the starting_node to the first list1 node

                 ex, starting_node -> 1 -> 2 -> 4 
                
                """

                # starting_node points to the next node within list1
                current.next = list1


                # move's list1 to its next node
                list1 = list1.next

            else:

                # starting_node points to the next node within list2
                current.next = list2

                # move's list2 to its next node
                list2 = list2.next

            current = current.next

        # attaches any nodes left after the loop 
        if list1:
            current.next = list1

        else:
            current.next = list2

        # return's the first real node, and what's linked to the first real node, which is the merged list of list1 and list2 is returned
        return starting_node.next