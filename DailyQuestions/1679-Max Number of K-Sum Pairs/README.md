# 1679-Max Number of K-Sum Pairs

**Approach One**
We can look for the **(k - x)** compliment of the number in the dictionary with its possiblity count p as a value. Whenever we find the number, we can decrease p. If we can't find any, then we'll store the number for its compliment to find it if it exists.

**Approach Two - Two Pointers**
After we sort the array in increasing order, we can use to pointers **left** and **right** to traverse from the beginning and the end of the array respectively. We can increase the count of our pairs when we find two pairs whose sum equals k. The traversal stops when left and right meet or when left's value exceeds that of k's.