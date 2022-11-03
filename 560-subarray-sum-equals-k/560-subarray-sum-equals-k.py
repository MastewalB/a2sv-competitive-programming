class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        total = 0
        hash_table = defaultdict(int)
        
        for num in nums:
            running_sum += num
            diff = running_sum - k
            if hash_table[diff] > 0:
                total += hash_table[diff]
            if running_sum == k:
                total += 1
            hash_table[running_sum] += 1
        return total