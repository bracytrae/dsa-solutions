class Solution {
    public int removeElement(int[] nums, int val) {

        // created a single counter var.
        int k = 0;

        // looped through the array
        for (int number : nums) {

            // if the number within the array is not equal to the value passed in, that number is put at the first position within the array, and the second number is put at the second position, and so on
            if (number != val) {
                nums[k] = number;
                k += 1;
            }
        }

        // how many valid values that pass the condition above are toward the beginning of the list nums which is known by k += 1
        return k;
    }
}
