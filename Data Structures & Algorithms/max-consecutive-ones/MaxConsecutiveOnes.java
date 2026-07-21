class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        // Track the current streak and the longest streak seen so far.
        int currentCount = 0;
        int maxCount = 0;

        for (int number : nums) {

            if (number == 1) {

                currentCount += 1;

                // Update the best result only when the current streak grows.
                maxCount = Math.max(maxCount, currentCount);

            } else {
                // A zero ends the current streak.
                currentCount = 0;
            }
        }

        return maxCount;
    }
}
