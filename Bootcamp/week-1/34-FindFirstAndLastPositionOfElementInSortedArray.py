class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        response = [-1, -1]
        if len(nums) == 0:
            return response
        left_index = right_index = index = 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                index = left_index = right_index = mid
                response[0] = response[1] = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        while left_index >= left:
            mid = left + (left_index - left) // 2
            if nums[mid] == target:
                response[0] = mid
                left_index = mid - 1
            else:
                left = mid + 1
        while right_index <= right:

            mid = right_index + (right - right_index) // 2
            if nums[mid] == target:
                response[1] = mid
                right_index = mid + 1
            else:
                right = mid - 1

        return response
