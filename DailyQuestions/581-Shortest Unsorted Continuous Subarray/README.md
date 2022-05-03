# 581-Shortest Unsorted Continuous Subarray

The Algorithm is to find the **disturbance** and identify and try to place elements in their correct place. 
Once we identify the distorted part in the array, we can find the *minimum* and *maximum* elements in it and check how much further to the left and right they stretch to(identifying the minimum and maximum indices that are affected).