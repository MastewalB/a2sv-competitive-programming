class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = nums[::]
        backward = nums[::]
        output = [1] * len(nums)
        
        for i in range(1, len(nums)):
            forward[i] *= forward[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            backward[j] *= backward[j + 1]
        
        for i in range(len(forward)):
            if i == 0:
                output[i] = backward[i + 1]
            elif i == len(forward) - 1:
                output[i] = forward[i -1]
            else:
                output[i] = forward[i -1] * backward[i + 1]
        return output