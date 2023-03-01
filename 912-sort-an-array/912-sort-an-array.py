class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(A, B):
            i, j = 0, 0
            S = []
            while i < len(A) or j < len(B):
                a = A[i] if i < len(A) else float("inf")
                b = B[j] if j < len(B) else float("inf")
                if a <= b:
                    S.append(a)
                    i += 1
                else:
                    S.append(b)
                    j += 1
            return S
        
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            N = len(nums)
            return merge(mergeSort(nums[:N // 2]), mergeSort(nums[N // 2:]))
        
        return mergeSort(nums)