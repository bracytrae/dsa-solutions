## Doubly Linked Lists 

doubly linked list - it is a 'concrete' data structure that stores 'elements' in a sequence of nodes; each 'node' contains a 'value' and 'references' to the 'previous' and 'next' node.

> note --> doubly linked lists are non-contiguous

## Creating a Doubly Linked List 

in a doubly linked list, each 'ListNode' has three 'attributes': 

1. val - stores the nodes value.

2. prev - points to the previous node.

3. next - points to the next node. 

<br>

> *creating its class blueprint*

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None 

# creates a class blueprint for possible doubly linked list objects due to 'structural' dissimilarity; they contain 'additional' attributes from singly linked lists and are 'distinct' in their data --> 'structure'.
```

```python
# structure  
      ↓
# node = [prev | value | next]
```
