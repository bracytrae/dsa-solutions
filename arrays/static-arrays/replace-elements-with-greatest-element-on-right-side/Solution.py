from typing import List

class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:

        # maintain a running maximum of the elements to the right
        # -1 is the required replacement for the final element
        max_to_right = -1

        # uses reverse traversal to move through the array from right to left.
        for index in range(len(arr) - 1, -1, -1):

            # preserve the current value before overwriting it in place
            current_value = arr[index]

            # replace the current element with the maximum to its right
            arr[index] = max_to_right

            # include the original current value in the next running maximum
            max_to_right = max(max_to_right, current_value)

        # return the array after the in-place transformation
        return arr
