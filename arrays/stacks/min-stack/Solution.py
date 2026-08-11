class MinStack:

    def __init__(self):

        # the main stack stores all values
        self.stack = []

        # the auxiliary stack stores the running minimum at each stack depth
        self.min_stack = []

    def push(self, val: int) -> None:

        # pushes the value onto the original stack
        self.stack.append(val)

        # also pushes the running minimum, keeping push() and getMin() at O(1) time
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:

            # the first value is also the first minimum
            self.min_stack.append(val)

    def pop(self) -> None:

        # pops the top value from both stacks
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:

        # peeks at the top value of the main stack
        return self.stack[-1]

    def getMin(self) -> int:

        # peeks at the running minimum on top of the auxiliary stack
        return self.min_stack[-1]
