class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        N, count = len(nums), 0
        for i in range(N):
            for j in range(i + 1, N):
                A, B = nums[i], nums[j]
                if len(A) + len(B) == len(target):
                    if A + B == target:
                        count += 1
                    if B + A == target:
                        count += 1
        
        return count