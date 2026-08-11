class Solution:
    def isValid(self, s: str) -> bool:

        # maps each closing bracket to its matching opening bracket
        matching_bracket = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # uses a stack to store unmatched opening brackets
        stack = []

        # traverses the input string from left to right
        for bracket in s:

            # dictionary membership identifies a closing bracket
            if bracket in matching_bracket:

                # an empty stack or mismatched top means the delimiters are invalid
                if not stack or stack[-1] != matching_bracket[bracket]:
                    return False

                # pop the matching opening bracket from the top of the stack
                else:
                    stack.pop()

            else:

                # push the opening bracket onto the stack
                stack.append(bracket)

        # the delimiters are balanced only when no unmatched brackets remain
        return not stack

