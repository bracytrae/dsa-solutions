## Singly Linked Lists 

singly linked list - it is a 'concrete' data structure that stores 'elements' in a sequence of nodes; each 'node' contains a 'value' and 'reference' to the 'next' node.

> note --> singly linked lists are non-contiguous

## Creating a Singly Linked List

in a singly linked list, each 'ListNode' object contains two 'attributes':

1. val - stores the nodes value.

2. next - points to the next node.

<br>

> *creating its class blueprint*

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None 

# creates a class blueprint for possible singly linked list objects due to 'structural' dissimilarity; they contain 'foundational' attributes for doubly linked lists and are 'distinct' in their data --> 'structure'.
```

```python
# structure  
      ↓
# node = [value | next]
```
## Traversal 

```python

head = ListNode1 

cur = head

while cur:
    cur = cur.next 

# cur
'''
ListNode1 starts at the head of the list 
'''
```












We start the traversal at the head of the list, which is ListNode1.

We assign it to a variable cur, denoting the current node we are at.

We execute the while loop until we reach the end of the list which is null.

In each iteration, we update cur to be the next node in the list by setting cur = cur.next.

The traversal runs in 
O
(
n
)
O(n) time where 
n
n is the number of nodes in the linked list.

# head --> exists so that you know where you are within the linked list. 

## Dummy Nodes 

## Operations of a Singly Linked List 