# Stacks 
stack - 'abstract' data type such that it follows 'LIFO' (last in, first out). 

<br>

common operations,

- push
- pop
- peek

<br>

```python
# think of a stack like "plates"

    [30] ← top
    [20]
    [10]

# you add and remove "plates" by the top
```
<br>

## Push

<br>

```python
def push(self, n):
    self.stack.append(n)

# adds a value at the top of the stack
```
*\*in this algorithim n represents the value that's added to the stack.*

<br>

## Pop 

<br>

```python
def pop(self):
    return self.stack.pop()

# removes a value from the top of the stack
```

<br>

## Peek 

<br>

```python
def peek(self):
    return self.stack[-1]

# views a value at the top of the stack
```

