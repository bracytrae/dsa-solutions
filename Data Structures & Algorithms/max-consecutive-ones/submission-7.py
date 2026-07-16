class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        """
        created two counter variables that compare the current count 
        of the most 1's counted consecutively vs the max_count of 1's 
        counted consecutively.
        """
    
        current_count = 0
        max_count = 0

        # loops through the list of integers 
        for number in nums:

            # if the number within the list is 1 it updates the current_count of 1's 
            if number == 1:

                current_count += 1
                max_count = max(max_count, current_count) # this automatically sets max_count to the max count of 1's counted consecutively

            # if it's not 1 it resets the current count back to 0 
            else:
                current_count = 0

        return max_count # once the list of integers is looped through the max_count of 1's counted consecutively is returned