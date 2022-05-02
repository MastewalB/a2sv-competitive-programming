# 905-SortArrayByParity

**Two Pointers**
1. We can traverse the array and assign the element to the left and right part of the new array by its parity.
2. Using the same approach, we can track the last index we have assigned an even element to and add a new one whenever we get another one, switching any odd element on its way.