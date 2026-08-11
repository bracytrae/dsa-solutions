from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # uses a dummy node so inserting the merged head needs no special case
        dummy_node = ListNode()

        """
            dummy_node ────┐
                            ──> [dummy node] ──> None
            tail ─────────┘
        """

        # tail always refers to the final node in the merged list
        tail = dummy_node

        # list1 and list2 are traversal pointers into the unmerged portions
        while list1 and list2:

            # compares the values of the two current nodes
            if list1.val <= list2.val:

                """
                 initially tail points to dummy_node, so the first insertion
                 connects dummy_node to the head of the merged list

                 ex, dummy_node -> 1 -> 2 -> 4
                """

                # appends the smaller current node from list1
                tail.next = list1


                # advances list1 to its next node
                list1 = list1.next

            else:

                # appends the smaller current node from list2
                tail.next = list2

                # advances list2 to its next node
                list2 = list2.next

            # advances the tail after each insertion
            tail = tail.next

        # attachs the remaining part of the non-empty list
        if list1:
            tail.next = list1

        else:
            tail.next = list2

        # skips the dummy node and return the head of the merged list
        return dummy_node.next
