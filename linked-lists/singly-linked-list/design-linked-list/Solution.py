# represents a node containing a value and a reference to the next node
class ListNode:
    def __init__(self, val=0):

        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):

        # dummy node before the first real node
        self.dummy_node = ListNode()

        # size stores the number of data nodes; the dummy node is not counted
        self.size = 0

    def get(self, index: int) -> int:

        # validate that index is within the list's bounds: 0 through size - 1
        if index < 0 or index >= self.size:
            return -1

        # initialize the traversal pointer at the head
        current = self.dummy_node.next

        # traverse to the node at index
        for i in range(index):
            current = current.next

        # return the data stored in the current node
        return current.val

    def addAtHead(self, val: int) -> None:

        # allocate the node to insert
        new_node = ListNode(val)

        # insert the new node between the dummy node and the old head
        new_node.next = self.dummy_node.next

        self.dummy_node.next = new_node

        # increment the list size after insertion
        self.size += 1

    def addAtTail(self, val: int) -> None:

        # allocate the node to insert
        new_node = ListNode(val)

        # initialize the traversal pointer at the dummy node
        current = self.dummy_node

        # traverse until current refers to the tail
        while current.next is not None:
            current = current.next

        # append the new node after the tail
        current.next = new_node

        # increment the list size after insertion
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        # insertion is valid from index 0 through size, inclusive
        if index < 0 or index > self.size:
            return

        # previous begins at the dummy node so index 0 needs no special case
        previous = self.dummy_node

        # traverse to the node immediately before the insertion position
        for i in range(index):
            previous = previous.next

        # allocate the node to insert
        new_node = ListNode(val)

        # insert the new node between previous and previous.next
        new_node.next = previous.next

        previous.next = new_node

        # increment the list size after insertion
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        # deletion is valid only for an existing index
        if index < 0 or index >= self.size:
            return

        # previous begins at the dummy node so index 0 needs no special case
        previous = self.dummy_node

        # traverse to the node immediately before the deletion target
        for i in range(index):
            previous = previous.next

        # store a reference to the target node
        node_to_delete = previous.next

        # unlink the target by connecting previous to the following node
        previous.next = node_to_delete.next

        # decrement the list size after deletion
        self.size -= 1
