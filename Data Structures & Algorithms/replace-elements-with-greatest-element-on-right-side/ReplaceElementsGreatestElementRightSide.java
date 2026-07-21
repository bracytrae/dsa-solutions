class Solution {

    public int[] replaceElements(int[] arr) {

        // stores the greatest number found to the right of the current index.
        // the last element has no numbers to its right, so it becomes -1.
        int greatestRight = -1;

        // moves through the array from right to left as opposed to the conventional way of looping through an array.
        for (int index = arr.length - 1; index >= 0; index--) {

            // saves the current value before replacing it.
            int currentValue = arr[index];

            // replaces the current element with the greatest value.
            // that was found to its right.
            // the first sequence in the iteration makes it a bit confusing to understand, but what is commented at the very start should help with clarification.
            
            arr[index] = greatestRight;

            // updates the greatestRight var for the next element to the left.
            // Compare the saved current value with the greatest value
            // already found and keep the larger one.
            
            greatestRight = Math.max(greatestRight, currentValue);
        }

        // Return the modified array.
        return arr;
    }
}
