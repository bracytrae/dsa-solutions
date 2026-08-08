# represents a node which contains a value and a pointer for a next node
class ListNode:
    def __init__(self, val=0):

        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):

        # starting node before the first real node
        self.starting_node = ListNode()

        # keeps track of the number of nodes in the linked list
        self.size = 0

    def get(self, index: int) -> int:

        # returns -1 if the index does not exist or is invalid
        if index < 0 or index >= self.size:
            return -1

        # starts at the first real node
        current = self.starting_node.next

        # points to the next node until current reaches the requested index
        for i in range(index):
            current = current.next

        # returns the value at that node 
        return current.val

    def addAtHead(self, val: int) -> None:

        # creates the new node
        new_node = ListNode(val)

        # the new node points to the old first node
        new_node.next = self.starting_node.next

        # starting node now points to the new first node
        self.starting_node.next = new_node

        # updates the number of nodes that are known to exist in the linked list
        self.size += 1

    def addAtTail(self, val: int) -> None:

        # creates the new node
        new_node = ListNode(val)

        # starts at the starting node
        current = self.starting_node

        # points to the next node until current reaches the last node
        while current.next is not None:
            current = current.next

        # makes the last node point to the new node
        current.next = new_node

        # updates the number of nodes that are known to exist in the linked list
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        # does nothing if the index is invalid 
        if index < 0 or index > self.size:
            return

        # begins before the first real node
        previous = self.starting_node

        # points to the node before the insertion position
        for i in range(index):
            previous = previous.next

        # creates the new node
        new_node = ListNode(val)

        # new node points to the next node
        new_node.next = previous.next

        # previous node points to the new node
        previous.next = new_node

        # updates the number of nodes that are known to exist in the linked list
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        # does nothing if the index is invalid 
        if index < 0 or index >= self.size:
            return

        # begins before the first real node
        previous = self.starting_node

        # points to the node before the node chosen for deletion
        for i in range(index):
            previous = previous.next

        # saves the node that will be deleted
        node_to_delete = previous.next

        # skips over the deleted node
        previous.next = node_to_delete.next

        # updates the number of nodes that are known to exist in the linked list
        self.size -= 1