from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:

        """
        You are keeping the scores for a baseball game with strange rules. 
        At the beginning of the game, you start with an empty record.
        """


        # This record will store all valid scores in order
        record = []

        # this iterates through operations that contains a list of strings 
        for op in operations:

            # If the op is "+", this adds a score equal to the sum of the previous two scores within the list
            if op == "+":
                record.append(record[-1] + record[-2])

            # If the operation is "D", this adds a score equal to double of the previous score
            elif op == "D":
                record.append(2 * record[-1])

            # If the operation is "C", this removes the previous score from the record since pop() removes the very last element within the list by default
            elif op == "C":
                record.pop()

            # else the operation is an integer score since no string's among the conditions "+"", "D", "C" remain
            else:
                record.append(int(op))

        # returns the total sum 
        return sum(record)

    