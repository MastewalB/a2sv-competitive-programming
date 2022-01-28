class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        result = nums[0]
        Max = (-sys.maxsize) - 1
        for i in range(1, k + 1):
            if i < len(nums):
                ret_val = self.maxResult(nums[i:], k)
                if ret_val > Max:
                    Max = ret_val
        result += Max
        return result


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = deque()
        queue.append(nums[0])

        for i in range(1, len(nums)):
            while queue and queue[0] < (i - k):
                queue.popleft()
            nums[i] += nums[queue[0]]
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        return nums[-1]
