class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i] == 0:
                j -= 1
            i += 1
        
        last = i
        i = j
        j = len(arr) - 1

        while i >= 0:
            arr[j] = arr[i]
            if arr[i] == 0 and i != last:
                j -= 1
                arr[j] = arr[i]
            i -= 1
            j -= 1
        