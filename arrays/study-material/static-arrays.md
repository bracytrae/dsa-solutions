# Static Arrays 

static arrays - cannot grow/shrink or store additional elements.

## Reading from a array 

<br>

> choosing a value within a array 

```python
# initializing a array 
myArray = [1, 2, 3]

# accessing a arbitrary element within a array
myArray = [i]
```
<br>

> traversing within a array 

```python
for i in range(len(myArray)):
    print(myArray[i])

# OR 

i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1
```
*the last element in a array is always at index n - 1, where n is the length of the array.*

## Deleting from a array 

<br>

> deleting from the end of a array 

```python
def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0

# sets the last value of the values chosen to 0 through usage of the algorithmic formula.
```
*in this algorithim length represents the number of values within the array passed in we wish to use.*

<br>

> deleting at a i'th index in a array

```python
def removeMiddle(arr, i, length):
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
# removes the element at index i by shifting every element after it one position to its left replacing it's position.
```
*in this algorithim length represents the same thing here, and i represents the index you wish to access.*

## Insertion 

<br>

> inserting at the end of a array

```python
def insertEnd(arr, n, length, capacity):
    if length < capacity: 
        arr[length] = n
# checks if the array has space, then inserts n into the next position at the end of the currently used values.
```
*in this algorithim length also represents the same thing here, capacity represents how big the array is, and n represents the new value you want to insert into the array.*

<br>

> inserting at the i'th index in a array

```python
def insertMiddle(arr, i, n, length): 
    for index in range(length - 1, i - 1, -1): # (start, stop, step): back 1
        arr[index + 1] = arr[index]
    arr[i] = n

# inserts a new a value at index i by shifting the element at i and every element after it one position to it's right
```
*in this algorithim length also represents the same thing here, i represents the index you wish to access, and n represents the new value you want to insert into the array.*

<br>