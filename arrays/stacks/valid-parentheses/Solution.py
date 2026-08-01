class Solution:
    def isValid(self, s: str) -> bool:

        # maps closing brackets to their matching opening brackets
        # key, value 
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # stack for storing opening brackets only 
        stack = []

        # go's through each character in the string 
        for c in s:

            # if this block run's first the function would return false immediately
            # if it's a closing bracket
            # this checks for the key
            if c in pairs:

            # if the stack is empty or the end of the stack's bracket does not match "c's" opening bracket, return False
                if not stack or stack[-1] != pairs[c]:
                    return False

                # else this removes the matching opening bracket
                else: 
                    stack.pop()

            else:

                # it has to be a opening bracket and it's added to the stack 
                stack.append(c)

        # valid only if every bracket matched correctly 
        return len(stack) == 0

    