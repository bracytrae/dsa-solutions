from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # tracks the current streak and the longest streak seen so far.
        current_count = 0
        max_count = 0

        for index in range(len(nums)):

            number = nums[index]

            if number == 1:

                current_count += 1

                # updates the best result only when the current streak grows.
                max_count = max(max_count, current_count)

            else:
                # a zero ends the current streak.
                current_count = 0

        return max_count
