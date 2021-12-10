class Solution:

    def selectionSort(self, arr, n):
        for i in range(n):
            minimum = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j

            arr[i], arr[minimum] = arr[minimum], arr[i]
            print(arr)
        return arr


arr = [1, 4, 23, 21, 6, 78, 1, 0]
sol = Solution()
sol.selectionSort(arr, 8)
