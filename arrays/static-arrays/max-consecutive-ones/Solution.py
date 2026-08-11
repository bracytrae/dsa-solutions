from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # track the current consecutive run and the maximum run seen so far
        current_streak = 0
        max_streak = 0

        for index in range(len(nums)):

            number = nums[index]

            if number == 1:

                current_streak += 1

                # update the maximum after extending the current streak
                max_streak = max(max_streak, current_streak)

            else:
                # a zero breaks the consecutive run
                current_streak = 0

        return max_streak
