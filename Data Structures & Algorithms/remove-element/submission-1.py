class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # created a single counter var. 
        k = 0

        # looped through the array 
        for number in nums:

            # if the number within the array is not equal to the value passed in, that number is put at the first position within the array, and the second number is put at the second position, and so on
            if number != val:
                nums[k] = number
                k += 1

        return k
        # how many valid values that pass the condition above are toward the beginning of the list nums which is known by k += 1

        
