class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        /*
         * created two counter variables that compare the current count
         * of 1's counted consecutively vs the max_count of 1's
         * counted consecutively.
         */

        int currentCount = 0;
        int maxCount = 0;

        // loops through the list of integers
        for (int number : nums) {

            // if the number within the list is 1 it updates the current_count of 1's
            if (number == 1) {

                currentCount += 1;

                // this automatically sets max_count to the max count of 1's counted consecutively
                maxCount = Math.max(maxCount, currentCount);

            // if it's not 1 it resets the current count back to 0
            } else {
                currentCount = 0;
            }
        }

        // once the list of integers is looped through the max_count of 1's counted consecutively is returned
        return maxCount;
    }
}
