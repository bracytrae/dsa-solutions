class Solution {
    public int removeElement(int[] nums, int val) {

        // k is both the number of kept values and the next position to fill.
        int k = 0;

        for (int index = 0; index < nums.length; index++) {

            int number = nums[index];

            // keep's the non-target values sorted at the beginning of the array.
            if (number != val) {
                nums[k] = number;
                k += 1;
            }
        }

        // the first k positions now contain every value not removed.
        return k;
    }
}