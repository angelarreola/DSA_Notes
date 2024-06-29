**<span style="font-weight:bold; color:rgb(0, 176, 80)">Input:</span>** A Sorted list of values.
**<span style="font-weight:bold; color:rgb(255, 192, 0)">Output:</span>** The position in the list of the target value we're searching or some sort of values indicate that the target doesn't exist in the list.

**<span style="font-weight:bold; color:rgb(0, 176, 240)">Steps:</span>**
1. Determine the middle position of the sorted list.
2. We compare the element in the middle position to the target element.
3. If the elements match we return the middle position and end. If they don't match we move to step 4.
4. We check whether the element in the middle position is smaller than the target element. If it is we go back to step 2 with a new list that goes from the middle position of the current list to the end of the current list.
5. If the element in the middle position is greater than the target element we go back to step 2 with a new list that goes from the start of the current list to the middle position of the current list.
6. Repeat this process until the target element is found or until a sub list contains only one element. If that single element sub list doesn't match the target element then we end the algorithm indicating that the elements doesn't exist in the list.