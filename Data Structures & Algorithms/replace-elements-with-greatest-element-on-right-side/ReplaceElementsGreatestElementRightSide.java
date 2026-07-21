class Solution {

    public int[] replaceElements(int[] arr) {

        // Scan from right to left while tracking the greatest value already seen.
        // The last element has nothing to its right, so its replacement is -1.
        int greatestRight = -1;

        for (int index = arr.length - 1; index >= 0; index--) { 

            // Save the current value before replacing it.
            int currentValue = arr[index]; 

            arr[index] = greatestRight;

            // Include the saved value when preparing the answer for the next index.
            greatestRight = Math.max(greatestRight, currentValue); 

        }

        return arr; 

    }
}
