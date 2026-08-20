# Dynamic Arrays 
dynamic arrays - 'can' grow/shrink and store 'additional' elements. 

<br>

> creating the class blueprint

```python
class DynamicArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

# creates a class blueprint for possible dynamic array objects due to behavior; dynamic arrays contain the same attributes as static arrays (e.g., capacity, length, & arr) but contain 'additive' -> behavior (e.g., resize, pushback).
```
*\*in the 'states', capacity represents how big the array is, length represents how many positions in the array are currently being used, and arr represents where the values are stored.*

<br>

## Insertion 

<br>

> inserting new values into an array

```python
def pushback(self, n):

    if self.length == self.capacity:
        self.resize()
        
    self.arr[self.length] = n
    self.length += 1

# pushback() inserts n into the array, and if length reaches capacity resize() is called.
```

<br>

## Resizing 

<br>

> doubling the capacity of an array

```python
 def resize(self): 

        self.capacity = 2 * self.capacity

        newArr = [0] * self.capacity

        for i in range(self.length):
            newArr[i] = self.arr[i]

        self.arr = newArr

# resize() doubles capacity, creates a new array with the increased capacity, uses the old array to replicate it's values into the new array, and makes the old array equal to the new array.
```

<br>












