from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # k is both the number of kept values and the next position to fill.
        k = 0

        for index in range(len(nums)):

            number = nums[index]

            # keep's the non-target values sorted at the beginning of the array.
            if number != val:
                nums[k] = number
                k += 1

        # the first k positions now contain every value not removed.
        return k
