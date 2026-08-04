class MinStack:

    def __init__(self):
        
        # the stack that store's all of the values 
        self.stack = []
        
        # the stack that store's the minimum values at each position 
        self.min_stack = []

    def push(self, val: int) -> None:

        # pushes the value onto the original stack 
        self.stack.append(val)

        # this also pushes the current minimum so the runtime becomes O(1) for min stack aswell
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:

            # if it is thefirst value, it is the deafult minimum
            self.min_stack.append(val)

    def pop(self) -> None:

        # remove's the top value from both stacks 
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:

        # return's the top value from the original stack
        return self.stack[-1]

    def getMin(self) -> int:

        # return's the top value from the min stack, which is the minimum
        return self.min_stack[-1]