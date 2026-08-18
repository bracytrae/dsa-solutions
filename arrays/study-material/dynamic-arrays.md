# Dynamic Arrays 

dynamic arrays - can grow/shrink and store additional elements. 

## Resize 

<br>

> why double the capacity? 

```python
class DynamicArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def resize(self): 

        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

# creates a class blueprint for possible dynamic array objects due to behavior; dynamic arrays contain the same attributes as static arrays (e.g., capacity, length, and arr) but contain extra behavior (e.g., resize, pushback).
```

*\*...*

<br>

> other operations
<br>

## Dynamic Array Insertion 

```python
# Insert n in the last position of the array
def pushback(self, n):
    if self.length == self.capacity:
        self.resize()
        
    # insert at next empty position
    self.arr[self.length] = n
    self.length += 1
```
<br>








