class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        begin, end = 0, len(nums) - 1

        while(begin <= end):
            pivot = math.floor((end - begin) // 2) + begin

            if nums[pivot] == target:
                return pivot

            if target < nums[pivot]:
                end = pivot - 1

            else:
                begin = pivot + 1

        return pivot if nums[pivot] > target else pivot + 1