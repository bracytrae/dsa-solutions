class Solution {
    public int removeElement(int[] nums, int val) {

        // k is both the number of kept values and the next position to fill.
        int k = 0;

        for (int number : nums) {

            // Keep non-target values packed at the beginning of the array.
            if (number != val) {
                nums[k] = number;
                k += 1;
            }
        }

        // The first k positions now contain every value that was not removed.
        return k;
    }
}
