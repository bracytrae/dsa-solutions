from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # write_index marks the next position for a retained value
        write_index = 0

        # index acts as the read pointer in this two-pointer algorithm
        for index in range(len(nums)):

            number = nums[index]

            # compact non-target values in place while preserving relative order
            if number != val:
                nums[write_index] = number
                write_index += 1

        # write_index is both the new logical length and the number of retained values
        return write_index
