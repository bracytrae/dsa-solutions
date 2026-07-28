class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:

        # stores the greatest number found to the right of the current index.
        # the last element has no numbers to its right, so it becomes -1.
        greatest_right = -1

        # moves through the array from right to left as opposed to the conventional way of looping through an array.
        for index in range(len(arr) - 1, -1, -1):

            # saves the current value before replacing it.
            current_value = arr[index]

            # replaces the current element with the greatest value.
            # that was found to its right.
            # the first sequence in the iteration makes it a bit confusing to understand, but what is commented at the very start should help with clarification.

            arr[index] = greatest_right

            # updates the greatest_right var for the next element to the left.
            # compares the saved current value with the greatest value
            # already found and keep the larger one.

            greatest_right = max(greatest_right, current_value)

        # returns the array modified by the algorithm
        return arr
