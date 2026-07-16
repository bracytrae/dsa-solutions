class Solution {

    public int[] replaceElements(int[] arr) {

        // [2, 4, 5, 3, 1, *2*]

        // the right most element within this algorithim must be -1 so it starts at -1
        int greatestRight = -1;

        // decrements down from 5 to 0 for the array
        for (int index = arr.length - 1; index >= 0; index--) { 

            // saves the original number 
            int currentValue = arr[index]; 

            // replace's the current number with the greatest number begans after the last element within the array changes to -1 sinces the algorithim begins at -1 and has yes to reach the operation that finds the max value.
            arr[index] = greatestRight;

            // this is what calculates the greatest number after every iteration starting at 5 and ending at 0 which covers the entire array
            greatestRight = Math.max(greatestRight, currentValue); 

        }

        return arr; 

    }
}