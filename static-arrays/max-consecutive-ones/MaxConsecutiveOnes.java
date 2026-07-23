class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        // tracks the current streak and the longest streak seen so far.
        int currentCount = 0;
        int maxCount = 0;

        for (int index = 0; index < nums.length; index++) {

            int number = nums[index];

            if (number == 1) {

                currentCount += 1;

                // updates the best result only when the current streak grows.
                maxCount = Math.max(maxCount, currentCount);

            } else {
                // a zero ends the current streak.
                currentCount = 0;
            }
        }

        return maxCount;
    }
}
