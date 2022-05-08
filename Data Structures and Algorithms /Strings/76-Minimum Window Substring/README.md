# 76-Minimum Window Substring

**Sliding Window**
Using sliding window, we can find the minimum substring that holds the letters in the *target*.
The key question is, while expanding or contracting the window, **"How do we keep track of the number of characters in it??"**

If we answer this question, we can easily move our window and try to optimize it when it holds enough of the target's characters.
To address this issue, we keep track of another dictionary that holds the count of each letter in the current window and another key variable, *formed*, that tells us how many of the target's characters are in the window.