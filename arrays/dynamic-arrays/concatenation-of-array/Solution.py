from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # input ex. nums = [1, 2, 3, 4]

        # stores the original array length as n
        n = len(nums)

        # creates an array twice the size of nums using the length of the original array
        # ex. ans = [0, 0, 0, 0, 0, 0, 0, 0]
        ans = [0] * (n * 2)

        # iterates through the length of the original array
        for i in range(n):

            # copies each number into the same position as the nums array which would be the original array passed in
            ans[i] = nums[i]

            # begins at the length of n which is the length of the original array and fills the remaining positions with the values of the nums array
            ans[i + n] = nums[i]

        return ans


"""

If an array is input for ex. nums = [1, 2, 3, 4]

the output would be nums = [1, 2, 3, 4, 1, 2, 3, 4]

"""
