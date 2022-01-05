class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = Deque()  # decreasing queue
        max_queue = Deque()  # increasing queue

        longest = 0
        left = 0
        right = 0

        while right < len(nums):

            while min_queue and nums[min_queue[-1]] <= nums[right]:
                min_queue.pop()
            min_queue.append(right)

            while max_queue and nums[max_queue[-1]] >= nums[right]:
                max_queue.pop()
            max_queue.append(right)

            if abs(nums[min_queue[0]] - nums[max_queue[0]]) <= limit:
                longest = max(longest, (right - left) + 1)
                right += 1
            else:
                left += 1
                if left > min_queue[0]:
                    min_queue.popleft()
                if left > max_queue[0]:
                    max_queue.popleft()

        return longest
