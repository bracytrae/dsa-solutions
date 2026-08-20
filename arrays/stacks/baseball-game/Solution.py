from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        """
            you are keeping the scores for a baseball game with strange rules,
            at the beginning of the game you start with an empty record.
        """

        # uses a stack to store the valid scores in insertion order
        score_stack = []

        # processes each operation from left to right
        for op in operations:

            # if the operation is "+", it pushes the sum of the top two scores onto the stack
            if op == "+":
                score_stack.append(score_stack[-1] + score_stack[-2])

            # if the operation is "D", it pushes double the top score onto the stack
            elif op == "D":
                score_stack.append(2 * score_stack[-1])

            # if the operation is "C", it pops the top score from the stack
            elif op == "C":
                score_stack.pop()

            # otherwise, it converts the operation to an integer and pushes it onto the stack
            else:
                score_stack.append(int(op))

        # return the sum of all scores remaining on the stack
        return sum(score_stack)

