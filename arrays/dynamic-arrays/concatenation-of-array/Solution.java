class Solution {
    public int[] getConcatenation(int[] nums) {

        // input ex. nums = [1, 2, 3, 4]

        // stores the original array length as n
        int n = nums.length;

        // creates an array twice the size of nums using the length of the original array 
        // ex. nums = [0, 0, 0, 0, 0, 0, 0, 0]
        int[] ans = new int[n * 2];



        // iterates through the length of the original array
        for (int i = 0; i < n; i++) {

            // copies each number into the same position as the num's array which would be the original array passed in
            ans[i] = nums[i];

            // begins at the length of n which is the length of the original array and fills the remaining positions with the values of the nums array
            ans[i + n] = nums[i];
        }

        return ans;
    }
}

/* 

If an array is input for ex. nums = [1, 2, 3, 4]

the output would be nums = [1, 2, 3, 4, 1, 2, 3, 4]

*/ 