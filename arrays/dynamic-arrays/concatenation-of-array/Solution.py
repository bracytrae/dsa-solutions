from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # n represents the length of the input array
        n = len(nums)

        # preallocates an output array with twice the input's length
        ans = [0] * (n * 2)

        # traverses every index in the input array
        for i in range(n):

            # copy the value into the first half at its original index
            ans[i] = nums[i]

            # copy the value into the second half using an offset of n
            ans[i + n] = nums[i]

        return ans


"""
    input:  nums = [1, 2, 3, 4]
    output: ans  = [1, 2, 3, 4, 1, 2, 3, 4]
"""
