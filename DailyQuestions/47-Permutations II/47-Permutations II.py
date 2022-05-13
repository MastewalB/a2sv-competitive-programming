class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        
        def perm(nums):
            nonlocal n
            if len(nums) == 1:
                    return [nums]
            order = set()
            response = []
            for index, num in enumerate(nums):
                if not num in order:
                    order.add(num)
                    ans = perm( nums[:index] + nums[index + 1:]  )
                    for arr in ans:
                        arr = [num] + arr
                        response.append(arr)
            return response
       
        return perm(nums)